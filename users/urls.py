from django.urls import path, include
from users.views import PaymentListAPIView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet

app_name = 'users'
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/users/', include(router.urls)),
    path('payments/', PaymentListAPIView.as_view(), name='list_payments'),
]