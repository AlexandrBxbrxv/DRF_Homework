from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materials.models import Course, Lesson
from materials.paginators import LessonPaginator, CoursePaginator
from materials.tasks import send_mail_about_course_update
from users.permissions import IsUserModerator, IsOwner
from materials.serializers import CourseSerializer, LessonSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [~IsUserModerator]
        elif self.action in ['retrieve', 'update']:
            self.permission_classes = [IsUserModerator | IsOwner]
        elif self.action == 'destroy':
            self.permission_classes = [~IsUserModerator | IsOwner]

        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        course = self.get_object()
        send_mail_about_course_update.delay(course=course.pk)
        return response


# CRUD для Lesson ###################################################
class LessonCreateAPI(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsUserModerator]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPI(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsUserModerator | IsOwner]
    pagination_class = LessonPaginator


class LessonRetrieveAPI(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsUserModerator | IsOwner]


class LessonUpdateAPI(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsUserModerator | IsOwner]


class LessonDestroyAPI(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ~IsUserModerator]
