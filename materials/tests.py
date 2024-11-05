from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from materials.models import Lesson, Course
from users.models import User, Subscription


# Тесты работы CRUD для Lesson ######################################
class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            id=1,
            email='test_user@bk.ru',
            password='123qwe',
        )
        self.client = APIClient()

    def test_lesson_create(self):
        """Тест создания урока."""

        self.client.force_authenticate(user=self.user)

        data = {
            "title": "test_lesson_create",
            "description": "test_lesson_create"
        }

        response = self.client.post(
            '/materials/lesson/create/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {
                'id': 1,
                'title': 'test_lesson_create',
                'preview': None,
                'description': 'test_lesson_create',
                'video_link': None,
                'course': None,
                'owner': 1
            }
        )

        self.assertTrue(Lesson.objects.filter(pk=1).exists())

    def test_lesson_list(self):
        """Тест просмотра списка уроков."""

        self.client.force_authenticate(user=self.user)

        Lesson.objects.create(
            title='test_list_lesson',
            description='test_list_lesson'
        )

        response = self.client.get(
            '/materials/lesson/list/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'count': 1,
             'next': None,
             'previous': None,
             'results': [{'course': None,
                          'description': 'test_list_lesson',
                          'id': 2,
                          'owner': None,
                          'preview': None,
                          'title': 'test_list_lesson',
                          'video_link': None}]}
        )

    def test_lesson_retrieve(self):
        """Тест просмотра подробностей урока."""

        self.client.force_authenticate(user=self.user)

        Lesson.objects.create(
            id=1,
            title='test_lesson_retrieve',
            description='test_lesson_retrieve',
            owner=self.user
        )

        response = self.client.get(
            '/materials/lesson/detail/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_update(self):
        """Тест изменения урока."""

        self.client.force_authenticate(user=self.user)

        Lesson.objects.create(
            id=1,
            title='test_lesson_retrieve',
            description='test_lesson_retrieve',
            owner=self.user
        )

        data = {
            "title": "test_lesson_update",
            "description": "test_lesson_update"
        }

        response = self.client.patch(
            '/materials/lesson/update/1/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                'id': 1,
                'title': 'test_lesson_update',
                'preview': None,
                'description': 'test_lesson_update',
                'video_link': None,
                'course': None,
                'owner': 1
            }
        )

    def test_lesson_delete(self):
        """Тест удаления урока."""

        self.client.force_authenticate(user=self.user)

        Lesson.objects.create(
            id=1,
            title='test_lesson_delete',
            owner=self.user
        )

        response = self.client.delete(
            '/materials/lesson/delete/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertTrue(not Lesson.objects.filter(pk=1).exists())


# Тесты для Subscription ############################################
class SubscriptionPermissionTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            id=1,
            email='test_user@bk.ru',
            password='123qwe',
        )

        self.course = Course.objects.create(
            id=1,
            title='test_course'
        )

    def test_subscribe_course(self):
        """Тест на подписку пользователя на курс."""

        self.client.force_authenticate(user=self.user)

        data = {
            "user": 1,
            "course": 1
        }

        response = self.client.post(
            '/users/sub_toggle/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'message': 'подписка добавлена'}
        )

        self.assertTrue(
            Subscription.objects.all().exists()
        )

    def test_unsubscribe_course(self):
        """Тест на удаление подписки пользователя на курс."""

        self.client.force_authenticate(user=self.user)

        Subscription.objects.create(
            pk=1,
            user=self.user,
            course=self.course
        )

        data = {
            "user": 1,
            "course": 1
        }

        response = self.client.post(
            '/users/sub_toggle/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'message': 'подписка удалена'}
        )

        self.assertTrue(
            not Subscription.objects.all().exists()
        )


# Тесты разрешений на действия с Lesson #############################
class UserPermissionTestCase(APITestCase):
    def setUp(self) -> None:
        moder_group = Group.objects.create(
            pk=1,
            name="moderator",
        )
        self.moder = User.objects.create(
            id=1,
            email='test_moder@bk.ru',
            password='123qwe',
        )
        moder_group.user_set.add(self.moder)
        self.moder.save()

        self.user = User.objects.create(
            id=2,
            email='test_user@bk.ru',
            password='123qwe',
        )

        self.other_user = User.objects.create(
            id=3,
            email='test_other_user@bk.ru',
            password='123qwe',
        )

        self.client = APIClient()

    def test_lesson_create_by_not_authorized_user(self):
        """Тест создания урока не авторизованным пользователем."""

        data = {
            "title": "test_lesson_create",
            "description": "test_lesson_create"
        }

        response = self.client.post(
            '/materials/lesson/create/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

        self.assertTrue(not Lesson.objects.filter(pk=1).exists())

    def test_lesson_create_by_moderator(self):
        """Тест создания урока модератором."""

        self.client.force_authenticate(user=self.moder)

        data = {
            "title": "test_lesson_create",
            "description": "test_lesson_create"
        }

        response = self.client.post(
            '/materials/lesson/create/',
            data=data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertTrue(not Lesson.objects.filter(pk=1).exists())

    def test_lesson_retrieve_by_not_owner_user(self):
        """Тест получения подробностей урока авторизованным пользователем, не являющимся владельцем урока."""

        self.client.force_authenticate(user=self.user)

        Lesson.objects.create(
            id=1,
            title='test_lesson_retrieve',
            owner=self.other_user
        )

        response = self.client.get(
            '/materials/lesson/detail/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_lesson_retrieve_by_not_owner_moderator(self):
        """Тест получения подробностей урока авторизованным модератором, не являющимся владельцем урока."""

        self.client.force_authenticate(user=self.moder)

        Lesson.objects.create(
            id=1,
            title='test_lesson_retrieve',
            owner=self.other_user
        )

        response = self.client.get(
            '/materials/lesson/detail/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
