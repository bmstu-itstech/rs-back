from django.contrib import admin

from rs_back.partners.forms import PartnerForm
from rs_back.partners.models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """
    Админ панель для партнёров
    """
    list_display = (
        'small_photo_tmb',
        'title',
        'link',
    )
    list_display_links = ('title', 'small_photo_tmb')
    readonly_fields = ('photo_tmb',)
    form = PartnerForm
