from django.contrib import admin

from hardathons.models import Hardathon


@admin.register(Hardathon)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'href',
        'quote',
        'background_image',
        'date',
        'start_date',
        'end_date',
        'result_date',
        'place',
        'media',
        'projects',
        'images',
        'documents',
        'partners',
    )
