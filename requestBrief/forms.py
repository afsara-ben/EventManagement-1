from django import forms
from .models import event_request


class requestForm(forms.ModelForm):
    class Meta:
        model = event_request
        fields = ('service', 'range', 'location', 'language', 'goal', 'job', 'size', 'otherservice',
                  'client_remote_work', 'request_status', 'client_name', )


