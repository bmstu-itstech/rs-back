from django.contrib import admin

from rs_back.hardathon.forms import HardathonForm, ProjectForm
from rs_back.hardathon.models import Hardathon, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Админ панель для проектов
    """
    list_display = (
        'small_photo_tmb',
        'title',
        'hardathon_title',
    )
    list_display_links = ('title', 'small_photo_tmb')
    readonly_fields = ('photo_tmb',)
    form = ProjectForm

    def hardathon_title(self, obj):
        return obj.hardathon.title

    hardathon_title.short_description = 'хардатон'


@admin.register(Hardathon)
class HardathonAdmin(admin.ModelAdmin):
    """
    Админ панель для хардатонов
    """
    list_display = (
        'small_photo_tmb',
        'title',
        'competition_task',
        'small_photo_tmb_org',
    )
    list_display_links = ('title', 'small_photo_tmb')
    filter_horizontal = ('partners',)
    readonly_fields = ('photo_tmb', 'photo_tmb_org')
    form = HardathonForm
