from django import forms
from .models import RSVP

class RSVPForm(forms.ModelForm):

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
    dietary_requirements = forms.ChoiceField(
        choices=DIETARY_CHOICES,
        widget=forms.RadioSelect
    )
    other_dietary_input = forms.CharField(
        max_length=255, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Specify other dietary requirements'})
    )
    attending_day2 = forms.ChoiceField(
        choices=DAY2_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    music_requests = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )

    class Meta:
        model = RSVP
        fields = ['name', 'will_attend', 'both_attending', 'dietary_requirements', 'attending_day2', 'music_requests']

    def clean(self):
        cleaned_data = super().clean()
        will_attend = cleaned_data.get("will_attend")
        dietary_requirements = cleaned_data.get("dietary_requirements")
        other_dietary_input = cleaned_data.get("other_dietary_input")

        if will_attend == 'True':  # 'True' is the string representation of True
            pass
        else:
            # If "No" is selected, we can ignore or clear the other fields
            for field in ['both_attending', 'dietary_requirements', 'attending_day2', 'music_requests']:
                cleaned_data[field] = None

        if dietary_requirements == 'Other' and not other_dietary_input:
            self.add_error('other_dietary_input', 'This field is required when "Other" is selected.')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        dietary_requirements = self.cleaned_data.get("dietary_requirements")
        other_dietary_input = self.cleaned_data.get("other_dietary_input")

        if dietary_requirements == 'Other':
            instance.dietary_requirements = other_dietary_input
        else:
            instance.dietary_requirements = dietary_requirements

        if commit:
            instance.save()
        return instance
