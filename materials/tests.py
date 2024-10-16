from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from .models import Course, Lesson, Subscription
from .serializers import CourseSerializer, LessonSerializer
from users.models import User
from rest_framework.test import APIClient

class CourseAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='password123',
            phone='1234567890'
        )
        self.course = Course.objects.create(
            name='Test Course',
            description='Test description',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name='Test Lesson',
            description='Test lesson description',
            video_link='https://youtube.com/watch?v=test',
            course=self.course,
            owner=self.user
        )
        self.client.force_authenticate(user=self.user)  # Аутентификация тестового пользователя

    def test_create_course(self):
        response = self.client.post('/courses/', {
            'name': 'New Course',
            'description': 'New description',
            'preview': None  # Или используйте правильный путь к изображению для теста
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_courses(self):
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # У нас есть 1 курс в тестах

    def test_subscribe_to_course(self):
        response = self.client.post(f'/courses/{self.course.id}/subscribe/')  # Эндпоинт для подписки
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_unsubscribe_from_course(self):
        # Сначала подписываемся
        self.client.post(f'/courses/{self.course.id}/subscribe/')
        response = self.client.post(f'/courses/{self.course.id}/unsubscribe/')  # Эндпоинт для отписки
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Subscription.objects.filter(user=self.user, course=self.course).exists())

    def test_course_with_subscription_status(self):
        response = self.client.get(f'/courses/{self.course.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('is_subscribed', response.data)
        self.assertFalse(response.data['is_subscribed'])  # Ожидаем, что по умолчанию пользователь не подписан
