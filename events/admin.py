from django.contrib import admin

from events.models import Event


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'date',
        'media_url',
        'album_url',
        'on_map_url',
        'docs_url',
        'registration_url',
    )
