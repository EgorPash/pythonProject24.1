from django.conf import settings
from django.db import models

class Course(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    preview = models.ImageField(upload_to='course_previews')
    description = models.TextField()

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['name']  # Можно настроить порядок сортировки по имени курса

    def __str__(self):
        return self.name

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='courses', on_delete=models.CASCADE)


class Lesson(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.TextField()
    preview = models.ImageField(upload_to='lesson_previews')
    video_link = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ['name']  # Можно настроить порядок сортировки по имени урока

    def __str__(self):
        return self.name

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='lessons', on_delete=models.CASCADE)