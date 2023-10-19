from django.db import models


class DietaryRequirement(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class RSVP(models.Model):
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
    ]

    DAY2_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Maybe', "I'll see how the head is")
    ]

    # GUEST 1
    name_1 = models.CharField(max_length=255)
    will_attend_1 = models.BooleanField("Are you attending?", default=False)
    dietary_requirements_1 = models.ManyToManyField(
        DietaryRequirement, blank=True, related_name='rsvps_dietary_1')
    other_dietary_input_1 = models.CharField(max_length=255, blank=True)
    attending_day2_1 = models.CharField(max_length=255, choices=DAY2_CHOICES)

    # GUEST 2
    name_2 = models.CharField(max_length=255)
    will_attend_2 = models.BooleanField(
        "Are you attending?", default=False, blank=True, null=True)
    dietary_requirements_2 = models.ManyToManyField(
        DietaryRequirement, blank=True, related_name='rsvps_dietary_2')
    other_dietary_input_2 = models.CharField(max_length=255, blank=True)
    attending_day2_2 = models.CharField(max_length=255, choices=DAY2_CHOICES)

    # GUEST 3
    name_3 = models.CharField(max_length=255)
    will_attend_3 = models.BooleanField(
        "Are you attending?", default=False, blank=True, null=True)
    dietary_requirements_3 = models.ManyToManyField(
        DietaryRequirement, blank=True, related_name='rsvps_dietary_3')
    other_dietary_input_3 = models.CharField(max_length=255, blank=True)
    attending_day2_3 = models.CharField(max_length=255, choices=DAY2_CHOICES)

    # GUEST 4
    name_4 = models.CharField(max_length=255)
    will_attend_4 = models.BooleanField(
        "Are you attending?", default=False, blank=True, null=True)
    dietary_requirements_4 = models.ManyToManyField(
        DietaryRequirement, blank=True, related_name='rsvps_dietary_4')
    other_dietary_input_4 = models.CharField(max_length=255, blank=True)
    attending_day2_4 = models.CharField(max_length=255, choices=DAY2_CHOICES)

    # GUEST 5
    name_5 = models.CharField(max_length=255)
    will_attend_5 = models.BooleanField(
        "Are you attending?", default=False, blank=True, null=True)
    dietary_requirements_5 = models.ManyToManyField(
        DietaryRequirement, blank=True, related_name='rsvps_dietary_5')
    other_dietary_input_5 = models.CharField(max_length=255, blank=True)
    attending_day2_5 = models.CharField(max_length=255, choices=DAY2_CHOICES)

    # MUSIC REQUESTS
    music_requests = models.TextField(blank=True)

    def __str__(self):
        return self.name_1
