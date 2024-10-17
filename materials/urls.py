from django.urls import path
from rest_framework.routers import DefaultRouter
from materials.views import SubscriptionAPIView

from materials.apps import MaterialsConfig
from materials.views import LessonListCreateAPIView, CourseViewSet, LessonRetrieveUpdateDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/', LessonListCreateAPIView.as_view(), name='list_create_lessons'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_lessons'),
    path('subscriptions/', SubscriptionAPIView.as_view(), name='manage_subscription'),
] + router.urls