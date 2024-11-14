import datetime

from django.utils import timezone

from users.models import User


def check_last_login():
    """Банит пользователей, которые не заходили больше месяца."""
    today = timezone.now().today().date()
    days_31 = datetime.timedelta(days=31)
    bannable_time = today + days_31
    # Логин через JWT, поэтому last_login = null, в обсуждении домашки сказали можно через date_joined реализовать
    users_for_ban = User.objects.filter(date_joined__gte=bannable_time)
    for user in users_for_ban:
        user.is_active = False
        user.save()
