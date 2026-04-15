from django.urls import path
from . import views
app_name = "events"

urlpatterns = [
    path('', views.CalendarView.as_view(), name="calendar"),
    path("event/<int:event_id>/details/", views.event_details, name="event_details"),
]