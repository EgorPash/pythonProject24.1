from rest_framework import serializers
from materials.models import Course, Lesson, Subscription
from materials.validators import validate_youtube_link


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'video_link', 'course']


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'lesson_count']

    def get_lesson_count(self, obj):
        return obj.lessons.count()

    def get_is_subscribed(self, obj):
        request = self.context.get('request')
        if request.user.is_authenticated:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False

class LessonSerializer(serializers.ModelSerializer):
    video_link = serializers.URLField(validators=[validate_youtube_link])

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'video_link', 'course']
