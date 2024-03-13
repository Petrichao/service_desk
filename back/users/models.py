from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Кастомный юзер, добавлен телеграм id, для взаимодействия с
    телеграммом"""
    telegram_id = models.IntegerField(unique=True,
                                      null=True, blank=True)

    def __str__(self):
        return self.username
