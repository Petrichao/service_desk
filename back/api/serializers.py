from rest_framework import serializers

from tickets.models import Tickets, Tags, Statuses, TelegramUsers


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        exclude = ("id",)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        exclude = ("id",)


class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        exclude = ("id",)


class TelegramUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUsers
        exclude = ("id",)
