from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from materials.models import Course, Subscription
from materials.models import Lesson
from materials.serializers import CourseSerializer
from users.permissions import IsOwner, IsModerator
from .serializers import LessonSerializer
from .paginators import StandardResultsSetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import create_product, create_price, create_checkout_session
from users.models import Payment
from .tasks import send_course_update_email


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.action in ['update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]  # Владельцы или менеджеры
        elif self.action == 'create':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Устанавливаем владельца

    def perform_update(self, serializer):
        course = serializer.save()
        subscribers = course.subscribers.all()  # Предполагается, что у Вас есть связь с подписчиками
        for subscriber in subscribers:
            send_course_update_email.delay(subscriber.email, course.name)


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]  # Только авторизованные пользователи
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated, ~IsModerator]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]  # Только владельцы могут обновлять и удалять

    def get_permissions(self):
        if self.request.method in ['GET', 'PATCH', 'PUT']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        else:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()

class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        course = get_object_or_404(Course, id=course_id)
        subscription, created = Subscription.objects.get_or_create(user=request.user, course=course)

        if created:
            message = 'Подписка добавлена'
        else:
            subscription.delete()
            message = 'Подписка удалена'

        return Response({"message": message})


class PaymentView(APIView):
    def post(self, request, *args, **kwargs):
        product_data = request.data.get('product')

        # Создаём продукт и цену в Stripe
        product = create_product(product_data['name'], product_data['description'])
        price = create_price(product.id, product_data['amount'])

        # Создаем сессию для оплаты
        session = create_checkout_session(price.id)

        # Сохраняем платёж
        payment_record = Payment.objects.create(
            user=request.user,
            paid_course=None,  # или заполните по необходимости
            amount=product_data['amount'],
            payment_method='stripe',  # Дополнительно
        )

        return Response({'url': session.url}, status=status.HTTP_201_CREATED)
