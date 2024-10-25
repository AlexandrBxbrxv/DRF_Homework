from rest_framework import serializers

from materials.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    course_lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('title', 'preview', 'description', 'course_lessons_count',)

    @staticmethod
    def get_course_lessons_count(course):
        return Lesson.objects.filter(course=course).count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
