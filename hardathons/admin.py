from django.contrib import admin

from hardathons.models import Hardathon


@admin.register(Hardathon)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'start_date',
        'end_date',
        'result',
        'place',
        'media',
        'projects',
        'images',
        'documents',
        'partners',
    )
