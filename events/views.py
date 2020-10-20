from django.shortcuts import render
from .models import EventModel


def home(request):
    events = EventModel.objects
    return render(request, 'events/home.html', {'events': events})