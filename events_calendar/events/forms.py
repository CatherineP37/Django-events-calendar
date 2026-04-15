from django.forms import ModelForm, DateInput
from events.models import Event
from django import forms

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "start_time"]
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Enter event title"}
            ),
            "start_time": DateInput(
                attrs={"type": "datetime-local",},
                format="%Y-%m-%dT%H:%M",
            ),
        }

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)       
            self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)

class EditEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "start_time"]
        widgets = {            
            "start_time": DateInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }

        def __init__(self, *args, **kwargs):
            super(EditEventForm, self).__init__(*args, **kwargs)       
            self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)