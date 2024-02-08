from django.contrib import admin
from .models import VolunteerUser, Event, Attendance, EventQrcode

# Register your models here.
admin.site.register(VolunteerUser)
admin.site.register(Event)
admin.site.register(Attendance)
admin.site.register(EventQrcode)