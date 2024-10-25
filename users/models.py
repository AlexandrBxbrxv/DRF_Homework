from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from materials.models import Course, Lesson

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


class Payment(models.Model):

    PAYMENT_METHOD_CHOICES = [
        ("cash", "наличные"),
        ("transfer to account", "перевод на счет"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, related_name='payment_user',
                             verbose_name='пользователь')
    payment_date = models.DateField(auto_now=True, verbose_name='дата оплаты')

    paid_course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, related_name='payment_course',
                                    verbose_name='оплаченный курс')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE, related_name='payment_lesson',
                                    verbose_name='оплаченный урок')

    payment_amount = models.IntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD_CHOICES, verbose_name='способ оплаты')
