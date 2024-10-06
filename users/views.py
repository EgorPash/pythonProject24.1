from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from users.models import Payment
from users.serializers import PaymentSerializer

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
