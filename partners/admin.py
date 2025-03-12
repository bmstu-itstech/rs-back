from django.contrib import admin

from partners.models import Partner


@admin.register(Partner)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'url',
        'logo',
    )
