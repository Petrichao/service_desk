from django.shortcuts import get_object_or_404, render

from tickets.models import Tickets, Statuses, Tags


def index(request):
    all_tickets = Tickets.objects.all()
    all_tags = Tags.objects.all()
    all_statuses = Statuses.objects.all()
    context = {
        'all_tickets': all_tickets,
        'all_statuses': all_statuses,
        'all_tags': all_tags
    }
    return render(request, "index.html", context)