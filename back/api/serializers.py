from rest_framework import serializers
from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model

from tickets.models import Tickets, Tags, Statuses


User = get_user_model()


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'username', 'first_name', 'last_name',
                  'telegram_id')


class TicketsSerializer(serializers.ModelSerializer):
    """Сериалайзер для тикетов"""
    class Meta:
        model = Tickets
        exclude = ("id",)


class TagsSerializer(serializers.ModelSerializer):
    """Сериалайзер для тэгов"""
    class Meta:
        model = Tags
        exclude = ("id",)


class StatusesSerializer(serializers.ModelSerializer):
    """Сериалайзер для статусов"""
    class Meta:
        model = Statuses
        exclude = ("id",)
