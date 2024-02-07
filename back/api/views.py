from rest_framework import viewsets

from tickets.models import Tickets, Tags, Statuses, TelegramUsers
from api.serializers import (
    TicketsSerializer,
    TagsSerializer,
    StatusesSerializer,
    TelegramUsersSerializer
)


class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class StatusesViewSet(viewsets.ModelViewSet):
    queryset = Statuses.objects.all()
    serializer_class = StatusesSerializer


class TelegramUsersViewSet(viewsets.ModelViewSet):
    queryset = TelegramUsers.objects.all()
    serializer_class = TelegramUsersSerializer
