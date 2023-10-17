# Generated by Django 4.2.6 on 2023-10-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0018_rename_attending_day2_rsvp_attending_day21_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsvp',
            old_name='attending_day21',
            new_name='attending_day2',
        ),
        migrations.RenameField(
            model_name='rsvp',
            old_name='other_dietary_input1',
            new_name='other_dietary_input',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='attending_day22',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='attending_day23',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='attending_day24',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='dietary_requirements1',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='dietary_requirements2',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='dietary_requirements3',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='dietary_requirements4',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='other_dietary_input2',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='other_dietary_input3',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='other_dietary_input4',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='dietary_requirements',
            field=models.ManyToManyField(blank=True, to='rsvp.dietaryrequirement'),
        ),
    ]
