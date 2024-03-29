# Generated by Django 4.2.9 on 2024-02-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluconnect', '0003_rename_user_email_volunteeruser_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteeruser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='volunteeruser',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
