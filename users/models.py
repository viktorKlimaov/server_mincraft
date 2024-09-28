from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.formfields import PhoneNumberField


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта',unique=True)
    phone = models.CharField(verbose_name='телефон', blank=True, null=True)
    country = models.CharField(verbose_name='Страна', default='Россия')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.email}'

