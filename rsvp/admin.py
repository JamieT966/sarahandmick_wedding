from django.contrib import admin
from .models import RSVP, DietaryRequirement, GuestName

class RSVPAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'will_attend', 'both_attending', 'not_attending_guest', 'display_dietary_requirements', 'other_dietary_input', 'attending_day2', 'music_requests',)
    list_filter = ('will_attend', 'both_attending', 'not_attending_guest', 'dietary_requirements', 'other_dietary_input', 'attending_day2')
    search_fields = ('name',)
    ordering = ('id',)

    def display_dietary_requirements(self, obj):
        return ", ".join([requirement.name for requirement in obj.dietary_requirements.all()])
    display_dietary_requirements.short_description = 'Dietary Requirements'

admin.site.register(RSVP, RSVPAdmin)
admin.site.register(DietaryRequirement)
admin.site.register(GuestName)

