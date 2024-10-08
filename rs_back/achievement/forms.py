from django import forms
from django.forms import FileInput, Textarea, TextInput, URLInput

from rs_back.achievement.models import Achievement


class AchievementForm(forms.ModelForm):
    """
    Форма для админ панели достижений. Нужна для того, чтобы расширить зону загрузки файлов
    """

    class Meta:
        model = Achievement
        fields = ('photo', 'title', 'description',
                  'photo_album_url', 'link_to_media',)
        widgets = {
            'photo': FileInput(attrs={'style': 'border: 1px solid #353535;'
                                               'padding: 5em; border-radius: 4px'}),
            'title': TextInput,
            'description': Textarea,
            'photo_album_url': URLInput,
            'link_to_media': URLInput,
        }
