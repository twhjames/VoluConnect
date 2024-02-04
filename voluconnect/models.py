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
    event_name = models.ForeignKey(Event, blank=True, null=True, on_delete=models.CASCADE)
    attendee = models.ForeignKey(VolunteerUser, blank=True, null=True, on_delete=models.CASCADE)
    ATS_STATUS = [('PRESENT', 'Present'), ('ABSENT', 'Absent')]
    ats_status = models.CharField(
        max_length = 7,
        choices = ATS_STATUS,
        default = 'ABSENT',
    )
    
    def __str__(self):
        return str(self.event_name) + ' ' + str(self.attendee) + ' Attendance'