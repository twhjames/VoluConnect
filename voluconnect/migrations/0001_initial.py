# Generated by Django 4.2.9 on 2024-02-08 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200, verbose_name='Event Name')),
                ('organisation', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('description', models.CharField(default='No Description', max_length=1000)),
                ('job_scope', models.CharField(default='No Job Scope', max_length=1000)),
                ('duration', models.IntegerField(default=0)),
                ('event_date', models.DateTimeField()),
                ('event_image', models.ImageField(default='default.jpg', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventQrcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qr_image_url', models.ImageField(blank=True, null=True, upload_to='')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voluconnect.event')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ats_status', models.CharField(choices=[('PRESENT', 'Present'), ('ABSENT', 'Absent')], default='ABSENT', max_length=7)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voluconnect.event')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voluconnect.volunteeruser')),
            ],
            options={
                'unique_together': {('event', 'user')},
            },
        ),
    ]
