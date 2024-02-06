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
from django.urls import path
from voluconnect import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('blog_details/', views.blog_details, name="blog_details"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('elements/', views.elements, name="elements"),
    path('login/', views.login, name="login"),
    path('register/', views.elements, name="register"),
    path('cards/', views.cards, name ="cards"),
    path('children/', views.children, name ="children"),
    path('gardening/', views.gardening, name ="gardening"),
    path('labour/', views.labour, name ="labour"),
    path('painting/', views.painting, name ="painting"),
    path('rations/', views.rations, name ="rations"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('attendance/', views.attendance, name="attendance"),
    path('events/', views.events, name="events"),
    path('forms/', views.forms, name="forms"),
    path('profile/', views.profile, name="profile"),
    path('add_event/', views.add_event, name="add_event"),
    path('export_events/', views.exportEventTablePDF, name="export_events"),
    path('delete_event/<int:pk>/', views.delete_event, name="delete_event"),
    path('get_event/<int:event_id>/', views.edit_event, name='get_event'),
    path('edit_event/', views.edit_event, name="edit_event"),
]
