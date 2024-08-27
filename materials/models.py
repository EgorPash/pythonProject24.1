from django.db import models

class Course(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    preview = models.ImageField(upload_to='course_previews')
    description = models.TextField()

class Lesson(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    description = models.TextField()
    preview = models.ImageField(upload_to='lesson_previews')
    video_link = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
