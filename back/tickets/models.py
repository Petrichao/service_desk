from django.db import models


# Create your models here.
class TelegramUsers(models.Model):
    telegram_id = models.IntegerField(
        verbose_name='Телеграм ID'
    )
    first_name = models.CharField(
        max_length=15,
        verbose_name='Имя'
    )
    second_name = models.CharField(
        max_length=15,
        verbose_name='Фамилия'
    )

    def __str__(self):
        return f'{self.second_name} {self.first_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Statuses(models.Model):
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
    title = models.CharField(
        max_length=100,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    author = models.ForeignKey(
        TelegramUsers,
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
