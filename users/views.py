import stripe
from django.conf import settings
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from users.models import Payment
from users.serializers import PaymentSerializer
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import create_product, create_price, create_checkout_session

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = {
        'payment_date': ['exact', 'lt', 'gt'],  # Фильтрация по дате
        'paid_course': ['exact'],                # Фильтрация по курсу
        'paid_lesson': ['exact'],                # Фильтрация по уроку
        'payment_method': ['exact'],             # Фильтрация по методу оплаты
    }
    ordering_fields = ['payment_date']  # Позволяет сортировать по дате
    ordering = ['payment_date']          # Сортировка по умолчанию

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()


class CheckoutSessionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_name = request.data.get('product_name')
        amount = request.data.get('amount')

        # Создание продукта и цены
        product = create_product(product_name)
        price = create_price(product.id, amount)

        # Создание сессии
        session = create_checkout_session(price.id, 'http://your-success-url.com','http://your-cancel-url.com')

        return Response({'url': session.url})