from django import forms
from django.forms import ModelForm
from .models import Event

# Create an add event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'number',
            'event_name',
            'organisation',
            'location',
            'event_date',
            'description',
            'job_scope',
            'duration',
            'event_image'
        )
        labels = {
            'number': 'Event Number',
            'event_name': 'Event',
            'organisation': 'Organisation',
            'location': 'Location',
            'event_date': 'Date & Time',
            'description': 'Description',
            'job_scope': 'Job Scope',
            'duration': 'Duration',
            'event_image': 'Event Image',

        }
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class':'form-control'}),
            'organisation': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'event_date': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'job_scope': forms.TextInput(attrs={'class':'form-control'}),
            'duration': forms.TextInput(attrs={'class':'form-control'}),
            'event_image': forms.FileInput(attrs={'class': 'form-control'}),
        }