# Generated by Django 4.2.6 on 2023-10-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0010_alter_rsvp_music_requests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='music_requests',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
