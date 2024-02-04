from django import forms
from django.forms import ModelForm
from .models import Event

# Create an add event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'event_name',
            'organisation',
            'location',
            'event_date'
        )
        labels = {
            'event_name': 'Event',
            'organisation': 'Organisation',
            'location': 'Location',
            'event_date': 'Date & Time'
        }
        widgets = {
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'organisation': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'event_date': forms.TextInput(attrs={'class':'form-control'}),
        }