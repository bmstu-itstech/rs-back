from django.db import models

from rs_back.core.models import ImageBaseModel


class Achievement(ImageBaseModel):
    """
    Модель достижения
    """
    title = models.CharField(
        'название',
        max_length=32,
        help_text='Максимум 32 символа',
    )
    description = models.TextField(
        'описание',
        max_length=220,
        help_text='Максимум 220 символов',
    )
    photo_album_url = models.URLField(
        'ссылка на фото-альбом',
        blank=True,
        max_length=128,
    )
    link_to_media = models.URLField(
        'ссылка на СМИ',
        blank=True,
        max_length=128,
    )

    class Meta:
        verbose_name = 'достижение'
        verbose_name_plural = 'достижения'

    @staticmethod
    def get_all_objects_by_id():
        return Achievement.objects.order_by('-id')
