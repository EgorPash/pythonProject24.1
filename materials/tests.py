from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from .models import Course, Lesson, Subscription
from .serializers import CourseSerializer, LessonSerializer
from users.models import User

class CourseTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='password123')
        self.course = Course.objects.create(name='Test Course', description='Course for testing', owner=self.user)
        self.lesson = Lesson.objects.create(name='Test Lesson', course=self.course, owner=self.user)

    def test_create_lesson(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('lessons:create'), {
            'name': 'New Lesson',
            'video_link': 'https://www.youtube.com/watch?v=test',
            'description': 'Lesson description',
            'course': self.course.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscription(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(reverse('manage_subscription'), {'course_id': self.course.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Subscription.objects.filter(user=self.user, course=self.course).exists())
