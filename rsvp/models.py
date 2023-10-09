from django.db import models

YES_NO_CHOICES = [
    (True, 'Yes'),
    (False, 'No')
]

DAY2_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Maybe', 'Maybe')
]

class DietaryRequirement(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class RSVP(models.Model):
    name = models.CharField(max_length=255)
    will_attend = models.BooleanField(choices=YES_NO_CHOICES)
    both_attending = models.BooleanField(null=True, blank=True)
    dietary_requirements = models.ManyToManyField(DietaryRequirement, blank=True)
    other_dietary_input = models.CharField(max_length=255, blank=True)
    attending_day2 = models.CharField(max_length=50, choices=DAY2_CHOICES, blank=True, null=True)
    music_requests = models.TextField(blank=True)

    def __str__(self):
        return self.name
