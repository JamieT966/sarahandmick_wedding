# Generated by Django 4.2.6 on 2023-10-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0014_guestname'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsvp',
            name='not_attending_guest',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
