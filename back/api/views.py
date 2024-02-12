from rest_framework import viewsets

from tickets.models import Tickets, Tags, Statuses
from api.serializers import (
    TicketsSerializer,
    TagsSerializer,
    StatusesSerializer,
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
