# Generated by Django 4.2.6 on 2023-10-07 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_remove_rsvp_other_dietary_requirements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='both_attending',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
