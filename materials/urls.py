from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateAPI, LessonListAPI

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateAPI.as_view(), name='lesson_create'),
    path('lesson/list/', LessonListAPI.as_view(), name='lesson_list'),
    path('lesson/detail/<int:pk>/', LessonListAPI.as_view(), name='lesson_detail'),
] + router.urls
