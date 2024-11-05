from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import VideoLinkValidator
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    @staticmethod
    def get_is_subscribed(course):
        result = Subscription.objects.filter(course=course).exists()
        return result


class CourseDetailSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()
    course_lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_course', many=True)

    class Meta:
        model = Course
        fields = ('title', 'preview', 'description', 'course_lessons_count', 'lessons', 'is_subscribed',)

    @staticmethod
    def get_course_lessons_count(course):
        return Lesson.objects.filter(course=course).count()

    @staticmethod
    def get_is_subscribed(course):
        result = Subscription.objects.filter(course=course).exists()
        return result
