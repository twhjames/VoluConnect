# Generated by Django 4.2.9 on 2024-02-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluconnect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
