from django import forms
from .models import RSVP, DietaryRequirement, GuestName

class RSVPForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RSVPForm, self).__init__(*args, **kwargs)
        self.fields['other_dietary_input'].label = ""
        self.fields['not_attending_guest'].label = ""

    YES_NO_CHOICES = [
        (True, 'Yes'),
        (False, 'No')
    ]

    DAY2_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Maybe', "I'll see how the head is")
    ]

    name = forms.ModelChoiceField(
        label="Name(s) on invite",
        queryset=GuestName.objects.all()
    )
    will_attend = forms.ChoiceField(
        label="Are you or anyone on the invite attending?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        required=True
    )
    both_attending = forms.ChoiceField(
        label="Is everyone on the invite attending?",
        choices=YES_NO_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )
    not_attending_guest = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name(s) of people not attending', 'class': 'no-label'}),
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
        fields = ['name', 'will_attend', 'both_attending', 'not_attending_guest', 'dietary_requirements', 'other_dietary_input', 'attending_day2', 'music_requests']
        labels = {
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
        
        if self.is_valid():
            guest_name = self.cleaned_data['name']
            guest_name.delete()

        if will_attend == 'True':  # 'True' is the string representation of True
            pass
        else:
            # If "No" is selected, we can ignore or clear the other fields
            for field in ['both_attending', 'dietary_requirements', 'attending_day2', 'music_requests']:
                cleaned_data[field] = None
            cleaned_data['dietary_requirements'] = []
        return cleaned_data