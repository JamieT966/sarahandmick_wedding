from django import forms
from .models import RSVP, DietaryRequirement

class RSVPForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RSVPForm, self).__init__(*args, **kwargs)
        self.fields['other_dietary_input'].label = ""
        self.fields['name2'].required = False

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
        label="Are you attending?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )
    both_attending = forms.ChoiceField(
        label="Is person two attending (if applicable)?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    dietary_requirements = forms.ModelMultipleChoiceField(
        label = "Do you have any other dietary requirements?",
        queryset=DietaryRequirement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    other_dietary_input = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Other Dietary Requirements', 'class': 'no-label'}),
        required=False
    )
    attending_day2 = forms.ChoiceField(
        label="Will you be attending day two?",
        choices=DAY2_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    music_requests = forms.CharField(
        label="Is there any music you want to hear on the night?",
        widget=forms.TextInput(),
        required=False
    )

    class Meta:
        model = RSVP
        fields = ['name', 'name2', 'will_attend', 'both_attending', 'dietary_requirements', 'other_dietary_input', 'attending_day2', 'music_requests']
        labels = {
            'name': 'Name on Invite',
            'name2': 'Name Two on Invite (if applicable)',
            'will_attend': 'Are you attending?',
            'both_attending': 'Is person two attending (if applicable)?',
            'dietary_requirements': 'Do you have any dietary requirements?',
            'other_dietary_input': 'Do you have any other dietary requirements?',
            'attending_day2': 'Will you be attending day two?',
            'music_requests': 'Is there any music you want to hear on the night?',
        }

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