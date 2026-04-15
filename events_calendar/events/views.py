from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta, datetime, date
import calendar
from django.urls import reverse
from django.shortcuts import get_object_or_404
from events.models import Event
from events.utils import Calendar

def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {"event": event}
    return render(request, 'events/event-details.html', context)