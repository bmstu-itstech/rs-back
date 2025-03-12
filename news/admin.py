from django.contrib import admin

from news.models import NewsRecord


@admin.register(NewsRecord)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'href',
        'image',
    )
