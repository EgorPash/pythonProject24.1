from django.urls import path, include
from users.views import PaymentListAPIView, PaymentCreateView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

app_name = 'users'
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('payments/', PaymentListAPIView.as_view(), name='list_payments'),
    path('payments/create/', PaymentCreateView.as_view(), name='create_payment'),
]