from django.urls import path
from . import views
app_name = "events"

urlpatterns = [
    path('', views.CalendarView.as_view(), name="calendar"),
    path("event/<int:event_id>/details/", views.event_details, name="event_details"),
    path('next_week/<int:event_id>/', views.next_week, name='next_week'),
    path('next_day/<int:event_id>/', views.next_day, name='next_day'),
    path("event/new/", views.new_event, name="new_event"),
    path("event/<int:event_id>/edit", views.edit_event, name="edit_event"),
]