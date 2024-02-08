"""
URL configuration for HackForGood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from voluconnect import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('course_details/<int:number>/', views.course_details, name='course_details'),
    path('elements/', views.elements, name="elements"),
    path('login/', views.login, name="login"),
    path('register/', views.elements, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('attendance/', views.attendance, name="attendance"),
    path('events/', views.events, name="events"),
    path('forms/', views.forms, name="forms"),
    path('profile/', views.profile, name="profile"),
    path('add_event/', views.add_event, name="add_event"),
    path('export_events/', views.exportEventTablePDF, name="export_events"),
    path('delete_event/<int:event_id>/', views.delete_event, name="delete_event"),
    path('get_event/<int:event_id>/', views.edit_event, name='get_event'),
    path('edit_event/', views.edit_event, name="edit_event"),
    path('take_event_attendance/<int:event_id>/', views.take_event_attendance, name='take_event_attendance'),
    path('qrGenerator/', views.qrGenerator, name="qrGenerator"),
    path('atsManagement/<int:event_id>/', views.atsManagement, name="atsManagement"),
    path('takeAttendance/<int:event_id>/<int:user_id>/', views.takeAttendance, name="takeAttendance"),
    path('attendance_login/', views.attendance_login, name="attendance_login"),
    path('attendance_result/', views.attendance_result, name="attendance_result"),
    path('form-creator/', include('form_creator.urls'), name="forms"),
    path('form-creator/forms/<int:number>-<slug:title>/response/', views.form_response, name='form_response'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
