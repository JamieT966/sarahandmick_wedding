from django.contrib import admin
from .models import RSVP, DietaryRequirement
import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    headers = [
        'Guest 1 Name', 'Will Attend (Guest 1)', 'Dietary Requirements (Guest 1)', 'Other Dietary Needs (Guest 1)', 'Attending Day 2 (Guest 1)',
        'Guest 2 Name', 'Will Attend (Guest 2)', 'Dietary Requirements (Guest 2)', 'Other Dietary Needs (Guest 2)', 'Attending Day 2 (Guest 2)',
        'Guest 3 Name', 'Will Attend (Guest 3)', 'Dietary Requirements (Guest 3)', 'Other Dietary Needs (Guest 3)', 'Attending Day 2 (Guest 3)',
        'Guest 4 Name', 'Will Attend (Guest 4)', 'Dietary Requirements (Guest 4)', 'Other Dietary Needs (Guest 4)', 'Attending Day 2 (Guest 4)',
        'Guest 5 Name', 'Will Attend (Guest 5)', 'Dietary Requirements (Guest 5)', 'Other Dietary Needs (Guest 5)', 'Attending Day 2 (Guest 5)',
        'Music Requests'
    ]
    writer.writerow(headers)

    for obj in queryset:
        row = []
        for i in range(1, 6):
            guest_data = [
                getattr(obj, f'name_{i}', ''),
                getattr(obj, f'will_attend_{i}', ''),
                ", ".join([dr.name for dr in getattr(obj, f'dietary_requirements_{i}').all()]),
                getattr(obj, f'other_dietary_input_{i}', ''), 
                getattr(obj, f'attending_day2_{i}', ''),
            ]
            row.extend(guest_data)

        row.append(getattr(obj, 'music_requests', '')) 
        writer.writerow(row)

    return response

export_to_csv.short_description = 'Export to CSV'


@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    # For Guest 1
    def get_guest_1_name(self, obj):
        return obj.name_1
    get_guest_1_name.short_description = 'Guest 1 Name'

    def get_will_attend_1(self, obj):
        return obj.will_attend_1
    get_will_attend_1.short_description = 'Will Attend (Guest 1)'

    def get_dietary_requirements_1(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_1.all()])
    get_dietary_requirements_1.short_description = 'Dietary Requirements (Guest 1)'

    def get_other_dietary_input_1(self, obj):
        return obj.other_dietary_input_1
    get_other_dietary_input_1.short_description = 'Other Dietary Needs (Guest 1)'

    def get_attending_day2_1(self, obj):
        return obj.attending_day2_1
    get_attending_day2_1.short_description = 'Attending Day 2 (Guest 1)'

    # Guest 2
    def get_guest_2_name(self, obj):
        return obj.name_2
    get_guest_2_name.short_description = 'Guest 2 Name'

    def get_will_attend_2(self, obj):
        return obj.will_attend_2
    get_will_attend_2.short_description = 'Will Attend (Guest 2)'

    def get_dietary_requirements_2(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_2.all()])
    get_dietary_requirements_2.short_description = 'Dietary Requirements (Guest 2)'

    def get_other_dietary_input_2(self, obj):
        return obj.other_dietary_input_2
    get_other_dietary_input_2.short_description = 'Other Dietary Needs (Guest 2)'

    def get_attending_day2_2(self, obj):
        return obj.attending_day2_2
    get_attending_day2_2.short_description = 'Attending Day 2 (Guest 2)'

    # Guest 3
    def get_guest_3_name(self, obj):
        return obj.name_3
    get_guest_3_name.short_description = 'Guest 3 Name'

    def get_will_attend_3(self, obj):
        return obj.will_attend_3
    get_will_attend_3.short_description = 'Will Attend (Guest 3)'

    def get_dietary_requirements_3(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_3.all()])
    get_dietary_requirements_3.short_description = 'Dietary Requirements (Guest 3)'

    def get_other_dietary_input_3(self, obj):
        return obj.other_dietary_input_3
    get_other_dietary_input_3.short_description = 'Other Dietary Needs (Guest 3)'

    def get_attending_day2_3(self, obj):
        return obj.attending_day2_3
    get_attending_day2_3.short_description = 'Attending Day 2 (Guest 3)'

    # Guest 4
    def get_guest_4_name(self, obj):
        return obj.name_4
    get_guest_4_name.short_description = 'Guest 4 Name'

    def get_will_attend_4(self, obj):
        return obj.will_attend_4
    get_will_attend_4.short_description = 'Will Attend (Guest 4)'

    def get_dietary_requirements_4(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_4.all()])
    get_dietary_requirements_4.short_description = 'Dietary Requirements (Guest 4)'

    def get_other_dietary_input_4(self, obj):
        return obj.other_dietary_input_4
    get_other_dietary_input_4.short_description = 'Other Dietary Needs (Guest 4)'

    def get_attending_day2_4(self, obj):
        return obj.attending_day2_4
    get_attending_day2_4.short_description = 'Attending Day 2 (Guest 4)'

    # Guest 5
    def get_guest_5_name(self, obj):
        return obj.name_5
    get_guest_5_name.short_description = 'Guest 5 Name'

    def get_will_attend_5(self, obj):
        return obj.will_attend_5
    get_will_attend_5.short_description = 'Will Attend (Guest 5)'

    def get_dietary_requirements_5(self, obj):
        return ", ".join([dr.name for dr in obj.dietary_requirements_5.all()])
    get_dietary_requirements_5.short_description = 'Dietary Requirements (Guest 5)'

    def get_other_dietary_input_5(self, obj):
        return obj.other_dietary_input_5
    get_other_dietary_input_5.short_description = 'Other Dietary Needs (Guest 5)'

    def get_attending_day2_5(self, obj):
        return obj.attending_day2_5
    get_attending_day2_5.short_description = 'Attending Day 2 (Guest 5)'


    list_display = (
        'get_guest_1_name', 'get_will_attend_1', 'get_dietary_requirements_1', 'get_other_dietary_input_1', 'get_attending_day2_1',
        'get_guest_2_name', 'get_will_attend_2', 'get_dietary_requirements_2', 'get_other_dietary_input_2', 'get_attending_day2_2',
        'get_guest_3_name', 'get_will_attend_3', 'get_dietary_requirements_3', 'get_other_dietary_input_3', 'get_attending_day2_3',
        'get_guest_4_name', 'get_will_attend_4', 'get_dietary_requirements_4', 'get_other_dietary_input_4', 'get_attending_day2_4',
        'get_guest_5_name', 'get_will_attend_5', 'get_dietary_requirements_5', 'get_other_dietary_input_5', 'get_attending_day2_5',
        'music_requests'
    )
    list_filter = ('will_attend_1', 'will_attend_2', 'will_attend_3', 'will_attend_4', 'will_attend_5',
                  )
    search_fields = ('name_1__name', 'name_2__name', 'name_3__name', 'name_4__name', 'name_5__name')
    ordering = ('-id',)

    actions = [export_to_csv]

admin.site.register(DietaryRequirement)
