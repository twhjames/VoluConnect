from django.db import models
    
class VolunteerUser(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Event(models.Model):
    event_name = models.CharField('Event Name', max_length=200)
    organisation = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    event_date = models.DateTimeField()
        
    def __str__(self):
        return self.event_name
    
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
