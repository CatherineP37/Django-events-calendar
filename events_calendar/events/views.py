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
from events.forms import EventForm, EditEventForm

def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {"event": event}
    return render(request, 'events/event_details.html', context)

def get_date(selected_day):
    if selected_day:
        year, month = (int(x) for x in selected_day.split("-"))
        return date(year, month, day=1)
    return datetime.today()

def previous_month(d):
    first = d.replace(day=1)
    previous_month = first - timedelta(days=1)
    month = "month=" + str(previous_month.year) + "-" + str(previous_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = "month=" + str(next_month.year) + "-" + str(next_month.month)
    return month

class CalendarView(generic.ListView):
    model = Event
    template_name = "events/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get("month", None))
        c = Calendar(d.year, d.month)
        html_calendar = c.formatmonth(withyear=True)
        context["calendar"] = mark_safe(html_calendar)
        context["previous_month"] = previous_month(d)
        context["next_month"] = next_month(d)
        return context

def new_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data["title"]        
        start_time = form.cleaned_data["start_time"]        
        Event.objects.get_or_create(           
            title=title,            
            start_time=start_time,            
        )
        return HttpResponseRedirect(reverse("events:calendar"))
    context = {"form":form}
    return render(request, "events/new_event.html", context)

def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EditEventForm(instance=event)
    if request.method == 'POST':
        form = EditEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('events:calendar')
    context = {"event":event, "form":form}
    return render(request, 'events/edit_event.html', context)

    