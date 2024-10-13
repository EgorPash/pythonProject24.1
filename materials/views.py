from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from materials.models import Course
from materials.models import Lesson
from materials.serializers import CourseSerializer
from users.permissions import IsOwner, IsModerator
from .serializers import LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]  # Владельцы или менеджеры
        else:
            self.permission_classes = [IsAuthenticated]  # Для просмотра списка
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Устанавливаем владельца


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated]  # Только авторизованные пользователи
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]  # Только владельцы могут обновлять и удалять

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)  # Убедитесь, что владелец установлен при обновлении
