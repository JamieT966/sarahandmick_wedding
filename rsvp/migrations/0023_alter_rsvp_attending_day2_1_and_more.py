# Generated by Django 5.0.3 on 2024-07-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0022_rsvp_attending_day2_5_rsvp_dietary_requirements_5_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='attending_day2_1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='attending_day2_2',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='attending_day2_3',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='attending_day2_4',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
        migrations.AlterField(
            model_name='rsvp',
            name='attending_day2_5',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255),
        ),
    ]
