from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urls import app_name

from materials.apps import MaterialsConfig
from materials.views import LessonListCreateAPIView, CourseViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonListCreateAPIView.as_view(), name='create lesson'),
   # path('lessons/', LessonListAPIView.as_view(), name='list lessons'),
   # path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='retrieve lesson'),
    # path('lessons/update/<int:pk>', LessonUpdateAPIView.as_view(), name='update lesson'),
    # path('lessons/delete/<int:pk>', LessonDestroyAPIView.as_view(), name='delete lesson'),
] + router.urls