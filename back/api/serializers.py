from rest_framework import serializers

from tickets.models import Tickets, Tags, Statuses


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
