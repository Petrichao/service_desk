from django.urls import path

from tickets.views import index

app_name = "tickets"

urlpatterns = [
    path("", index, name="index"),
]
