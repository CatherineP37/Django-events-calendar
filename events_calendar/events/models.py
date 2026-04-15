from datetime import datetime
from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("events:event-detail", args=(self.id,))
    
    @property
    def get_html_url(self):
        url = reverse("events:event_details", args=(self.id,))
        return f'<a href="{url}">{self.title}</a>'