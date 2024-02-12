from django.urls import include, path
from rest_framework.routers import DefaultRouter

from back.api.views import (
    TagsViewSet,
    StatusesViewSet,
    TicketsViewSet
)


router_v1 = DefaultRouter()

router_v1.register('tags', TagsViewSet, basename='tags')
router_v1.register('statuses', StatusesViewSet, basename='statuses')
router_v1.register('tickets', TicketsViewSet, basename='tickets')

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
