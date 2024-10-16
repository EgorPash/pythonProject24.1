from django.urls import path, include
from materials.views import PaymentView
from users.views import PaymentListAPIView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

app_name = 'users'
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('payments/', PaymentView.as_view(), name='create_payment'),
    path('payments/', PaymentListAPIView.as_view(), name='list_payments'),
]