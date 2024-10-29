from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from users.permissions import IsUserModerator
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            self.permission_classes = [~IsUserModerator]
        elif self.action in ['retrieve', 'update']:
            self.permission_classes = [IsUserModerator]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


# CRUD для Lesson ###################################################
class LessonCreateAPI(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [~IsUserModerator]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPI(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPI(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPI(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [~IsUserModerator]
