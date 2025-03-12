from django.contrib import admin

from achievements.models import Achievement


@admin.register(Achievement)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'album_url',
        'media_url',
        'image',
    )
