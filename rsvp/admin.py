from django.contrib import admin
from .models import RSVP, DietaryRequirement

@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('name_1', 'will_attend_1', 'display_dietary_requirements_1', 'other_dietary_input_1', 'attending_day2_1',
                    'name_2', 'will_attend_2', 'display_dietary_requirements_2', 'other_dietary_input_2', 'attending_day2_2',
                    'name_3', 'will_attend_3', 'display_dietary_requirements_3', 'other_dietary_input_3', 'attending_day2_3',
                    'name_4', 'will_attend_4', 'display_dietary_requirements_4', 'other_dietary_input_4', 'attending_day2_4',
                    'name_5', 'will_attend_5', 'display_dietary_requirements_5', 'other_dietary_input_5', 'attending_day2_5',
                    'music_requests'
                   )
    list_filter = ('will_attend_1', 'will_attend_2', 'will_attend_3', 'will_attend_4', 'will_attend_5',
                  )
    search_fields = ('name_1__name', 'name_2__name', 'name_3__name', 'name_4__name', 'name_5__name')
    ordering = ('-id',)

    
    def display_dietary_requirements_1(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_1.all()])
    display_dietary_requirements_1.short_description = 'Dietary Requirements 1'

    def display_dietary_requirements_2(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_2.all()])
    display_dietary_requirements_2.short_description = 'Dietary Requirements 2'

    def display_dietary_requirements_3(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_3.all()])
    display_dietary_requirements_3.short_description = 'Dietary Requirements 3'

    def display_dietary_requirements_4(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_4.all()])
    display_dietary_requirements_4.short_description = 'Dietary Requirements 4'

    def display_dietary_requirements_5(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_5.all()])
    display_dietary_requirements_5.short_description = 'Dietary Requirements 5'

admin.site.register(DietaryRequirement)
