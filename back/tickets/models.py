from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

User = get_user_model()


class Statuses(models.Model):
    """Модель статусов"""
    name = models.CharField(
        max_length=15,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Tags(models.Model):
    """Модель тегов"""
    name = models.CharField(
        max_length=15,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Tickets(models.Model):
    """Модель тикетов"""
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор'
    )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Статус'
    )
    tag = models.ForeignKey(
        Tags,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тег'
    )

    def __str__(self):
        return f'{self.id} - {self.title}'

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикеты"
