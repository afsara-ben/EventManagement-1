from django import forms
from .models import *


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields  =('event_name','event_venue', 'event_type','event_budget', )


