import datetime
from smtplib import SMTPException

from celery import shared_task
from django.core.mail import send_mail
from rest_framework.response import Response

from config.settings import EMAIL_HOST_USER
from users.models import Subscription


@shared_task(bind=True, max_retries=5)
def send_mail_about_course_update(self, course):
    """Отправляет сообщение на почту всем пользователям подписанным на курс."""
    now = datetime.datetime.now()
    difference = datetime.timedelta(hours=4)
    # Проверка на прохождение 4 часов после последнего обновления
    if course.last_update + difference > now:
        # Перезапуск через час
        raise self.retry(countdown=3600)

    if Subscription.objects.filter(course=course).exists():
        subscribed_users_emails = []
        subscriptions = Subscription.objects.filter(course=course)
        for subscription in list(subscriptions):
            subscribed_users_emails.append(subscription.user.email)
        try:
            send_mail(
                subject='Обновление курса',
                message=f'Курс {course} был обновлен, советуем его проверить',
                from_email=EMAIL_HOST_USER,
                recipient_list=subscribed_users_emails
            )
        except SMTPException as e:
            raise self.retry(exc=e, countdown=3600)
