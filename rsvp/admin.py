from django.contrib import admin
from .models import RSVP
# Register your models here.

class RSVPAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'will_attend', 'dietary_requirements', 'both_attending', 'attending_day2')
    list_filter = ('will_attend', 'both_attending', 'dietary_requirements', 'attending_day2')
    search_fields = ('name',)
    ordering = ('id',)

admin.site.register(RSVP, RSVPAdmin)
