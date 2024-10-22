from rest_framework.routers import DefaultRouter

from materials.views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls
