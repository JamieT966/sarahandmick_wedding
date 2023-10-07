from django.db import models

YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
]

DIETARY_CHOICES = [
    ('Coeliac', 'Coeliac'),
    ('Lactose', 'Lactose Intolerant'),
    ('Vegetarian', 'Vegetarian'),
    ('Vegan', 'Vegan'),
    ('Other', 'Other')
]

DAY2_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Maybe', 'Maybe')
]

class RSVP(models.Model):

    name = models.CharField(max_length=255)
    will_attend = models.BooleanField(choices=YES_NO_CHOICES)
    both_attending = models.BooleanField(null=True, blank=True)
    dietary_requirements = models.CharField(max_length=50, choices=DIETARY_CHOICES)
    attending_day2 = models.CharField(max_length=50, choices=DAY2_CHOICES, blank=True, null=True)
    music_requests = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name