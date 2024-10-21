from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from .validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[validate_youtube_link])

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'video_link', 'course']


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'lesson_count', 'lessons', 'is_subscribed']

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False