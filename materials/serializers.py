from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import VideoLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    course_lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_course', many=True)

    class Meta:
        model = Course
        fields = ('title', 'preview', 'description', 'course_lessons_count', 'lessons',)

    @staticmethod
    def get_course_lessons_count(course):
        return Lesson.objects.filter(course=course).count()
