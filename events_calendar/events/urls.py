from django.urls import path
from . import views
app_name = "events"

urlpatterns = [
    path("event/<int:event_id>/details/", views.event_details, name="event_details"),
]