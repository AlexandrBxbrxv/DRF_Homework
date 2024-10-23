from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    nickname = models.CharField(max_length=50, **NULLABLE, verbose_name='ник')

    email = models.EmailField(unique=True, verbose_name='email')
    token = models.CharField(max_length=50, **NULLABLE, verbose_name='token')

    phone_number = models.CharField(
        max_length=15,
        **NULLABLE,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        verbose_name='номер телефона'
    )
    city = models.CharField(max_length=150, **NULLABLE, verbose_name='город')
    avatar = models.ImageField(upload_to='users/avatars', **NULLABLE, verbose_name='аватарка')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
