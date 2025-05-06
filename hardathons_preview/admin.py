from django.contrib import admin

from hardathons_preview.models import HardathonPreview


@admin.register(HardathonPreview)
class EventsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'href',
        'photo',
        'title',
    )
