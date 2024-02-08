from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
    
class VolunteerUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email

class Event(models.Model):
    number = models.IntegerField(blank=True, null=True)
    event_name = models.CharField('Event Name', max_length=200)
    organisation = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default = 'No Description')
    job_scope = models.CharField(max_length=1000, default = 'No Job Scope')
    duration = models.IntegerField(default=0)
    event_date = models.DateTimeField()
    event_image = models.ImageField(upload_to = 'images/', default='default.jpg')
        
    def __str__(self):
        return '{} - {}'.format(self.number, self.event_name)

class Attendance(models.Model):
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(VolunteerUser, blank=True, null=True, on_delete=models.CASCADE)
    attendance_options = [('PRESENT', 'Present'), ('ABSENT', 'Absent')]
    ats_status = models.CharField(
        max_length = 7,
        choices = attendance_options,
        default = 'ABSENT',
    )
    
    def __str__(self):
        return str(self.event.event_name) + ' ' + str(self.user.user_name) + ' Attendance'
    
    class Meta:
        unique_together = ('event', 'user')  # Ensures each user has only one attendance record per event

class EventQrcode(models.Model):
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.CASCADE)
    qr_image_url = models.ImageField(null=True, blank=True, upload_to='')

    def __str__(self):
        return str(self.event) + '-QRcode'
