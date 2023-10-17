from django import forms
from .models import RSVP, DietaryRequirement

class RSVPForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RSVPForm, self).__init__(*args, **kwargs)
        self.fields['other_dietary_input_1'].label = ""
        self.fields['other_dietary_input_2'].label = ""
        self.fields['other_dietary_input_3'].label = ""
        self.fields['other_dietary_input_4'].label = ""
        self.fields['other_dietary_input_5'].label = ""
        self.fields['will_attend_2'].required = False
        self.fields['will_attend_3'].required = False
        self.fields['will_attend_4'].required = False
        self.fields['will_attend_5'].required = False

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
    name_1 = forms.CharField(
        label="Guest 1 Name",
        widget=forms.TextInput(),
        required=True
    )
    
    will_attend_1 = forms.ChoiceField(
        choices=[(True, 'Yes'), (False, 'No')],
        widget=forms.RadioSelect,
        label="Are you attending?"
    )

    dietary_requirements_1 = forms.ModelMultipleChoiceField(
        label = "1. Do you have any other dietary requirements?",
        queryset=DietaryRequirement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    other_dietary_input_1 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Other Dietary Requirements', 'class': 'no-label'}),
        required=False
    )

    attending_day2_1 = forms.ChoiceField(
        label="1. Will you be attending day two?*",
        choices=DAY2_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    # GUEST 2
    name_2 = forms.CharField(
        label="Guest 2 Name (If Applicable)",
        widget=forms.TextInput(),
        required=False
    )
    
    will_attend_2 = forms.ChoiceField(
        choices=[(True, 'Yes'), (False, 'No')],
        widget=forms.RadioSelect,
        label="Are you attending?"
    )

    dietary_requirements_2 = forms.ModelMultipleChoiceField(
        label = "2. Do you have any other dietary requirements?",
        queryset=DietaryRequirement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    other_dietary_input_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Other Dietary Requirements', 'class': 'no-label'}),
        required=False
    )

    attending_day2_2 = forms.ChoiceField(
        label="2. Will you be attending day two?*",
        choices=DAY2_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    # GUEST 3
    name_3 = forms.CharField(
        label="Guest 3 Name (If Applicable)",
        widget=forms.TextInput(),
        required=False
    )
    
    will_attend_3 = forms.ChoiceField(
        choices=[(True, 'Yes'), (False, 'No')],
        widget=forms.RadioSelect,
        label="Are you attending?"
    )

    dietary_requirements_3 = forms.ModelMultipleChoiceField(
        label = "3. Do you have any other dietary requirements?",
        queryset=DietaryRequirement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    other_dietary_input_3 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Other Dietary Requirements', 'class': 'no-label'}),
        required=False
    )

    attending_day2_3 = forms.ChoiceField(
        label="3. Will you be attending day two?*",
        choices=DAY2_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    # GUEST 4
    name_4 = forms.CharField(
        label="Guest 4 Name (If Applicable)",
        widget=forms.TextInput(),
        required=False
    )
    
    will_attend_4 = forms.ChoiceField(
        choices=[(True, 'Yes'), (False, 'No')],
        widget=forms.RadioSelect,
        label="Are you attending?"
    )

    dietary_requirements_4 = forms.ModelMultipleChoiceField(
        label = "4. Do you have any other dietary requirements?",
        queryset=DietaryRequirement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    other_dietary_input_4 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Other Dietary Requirements', 'class': 'no-label'}),
        required=False
    )

    attending_day2_4 = forms.ChoiceField(
        label="4. Will you be attending day two?*",
        choices=DAY2_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    # GUEST 5
    name_5 = forms.CharField(
        label="Guest 5 Name (If Applicable)",
        widget=forms.TextInput(),
        required=False
    )
    
    will_attend_5 = forms.ChoiceField(
        choices=[(True, 'Yes'), (False, 'No')],
        widget=forms.RadioSelect,
        label="Are you attending?"
    )

    dietary_requirements_5 = forms.ModelMultipleChoiceField(
        label = "5. Do you have any other dietary requirements?",
        queryset=DietaryRequirement.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    other_dietary_input_5 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Other Dietary Requirements', 'class': 'no-label'}),
        required=False
    )

    attending_day2_5 = forms.ChoiceField(
        label="5. Will you be attending day two?*",
        choices=DAY2_CHOICES,
        widget=forms.RadioSelect,
        required=False
    )

    # MUSIC REQUESTS FOR ALL ON INVITE
    music_requests = forms.CharField(
        label="Is there any music you want to hear on the night?",
        widget=forms.TextInput(),
        required=False
    )

    class Meta:
        model = RSVP
        fields = ['name_1', 'will_attend_1', 'dietary_requirements_1', 'other_dietary_input_1', 'attending_day2_1',
                  'name_2', 'will_attend_2', 'dietary_requirements_2', 'other_dietary_input_2', 'attending_day2_2',
                  'name_3', 'will_attend_3', 'dietary_requirements_3', 'other_dietary_input_3', 'attending_day2_3',
                  'name_4', 'will_attend_4', 'dietary_requirements_4', 'other_dietary_input_4', 'attending_day2_4',
                  'name_5', 'will_attend_5', 'dietary_requirements_5', 'other_dietary_input_5', 'attending_day2_5',
                  'music_requests'
                  ]
