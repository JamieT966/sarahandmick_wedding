# Generated by Django 4.2.6 on 2023-10-12 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0016_remove_rsvp_both_attending_remove_rsvp_name2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsvp',
            name='name',
        ),
        migrations.RemoveField(
            model_name='rsvp',
            name='will_attend',
        ),
        migrations.AddField(
            model_name='rsvp',
            name='name1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='name1', to='rsvp.guestname'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsvp',
            name='name2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name2', to='rsvp.guestname'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='name3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name3', to='rsvp.guestname'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='name4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name4', to='rsvp.guestname'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='will_attend1',
            field=models.BooleanField(default=False, verbose_name='Are you attending?'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='will_attend2',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Are you attending?'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='will_attend3',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Are you attending?'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='will_attend4',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Are you attending?'),
        ),
    ]
