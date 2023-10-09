from django import forms
from .models import RSVP, DietaryRequirement

class RSVPForm(forms.ModelForm):
    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
    ]

    DAY2_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Maybe', 'Maybe')
    ]

    will_attend = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )
    both_attending = forms.ChoiceField(
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    dietary_requirements = forms.ModelMultipleChoiceField(
        queryset=DietaryRequirement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    other_dietary_input = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Other Dietary Requirements'}),
        required=False
    )
    attending_day2 = forms.ChoiceField(
        choices=DAY2_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    music_requests = forms.CharField(
        widget=forms.TextInput(),
        required=False
    )

    class Meta:
        model = RSVP
        fields = ['name', 'name2', 'will_attend', 'both_attending', 'dietary_requirements', 'other_dietary_input', 'attending_day2', 'music_requests']

    def clean(self):
        cleaned_data = super().clean()
        will_attend = cleaned_data.get("will_attend")

        if will_attend == 'True':  # 'True' is the string representation of True
            pass
        else:
            # If "No" is selected, we can ignore or clear the other fields
            for field in ['both_attending', 'dietary_requirements', 'attending_day2', 'music_requests']:
                cleaned_data[field] = None
            cleaned_data['dietary_requirements'] = []
        return cleaned_data