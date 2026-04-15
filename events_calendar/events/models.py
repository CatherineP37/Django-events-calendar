from datetime import datetime
from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
