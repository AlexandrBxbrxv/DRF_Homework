from django.core.management import BaseCommand

from users.models import User, Payments
from materials.models import Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Создает объект модели Payments"""

        # создаем User для Payments
        User.objects.filter(pk=1).delete()
        User.objects.create(
            pk=1,
            nickname='user_1',
            email='user@123.com',
        )
        user = User.objects.get(pk=1)

        # создаем Lesson для Payments
        Lesson.objects.filter(pk=1).delete()
        Lesson.objects.create(
            pk=1,
            title='Lesson 1',
            description='Cool lesson'
        )
        lesson = Lesson.objects.get(pk=1)

        # создаем Payments
        Payments.objects.filter(pk=1).delete()
        Payments.objects.create(
            pk=1,
            user=user,
            paid_lesson=lesson,
            payment_amount=1000,
            payment_method='cash'
        )
