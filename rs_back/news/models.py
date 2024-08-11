from django.db import models

from rs_back.core.models import ImageBaseModel


class News(ImageBaseModel):
    """
    Модель новости
    """
    title = models.CharField(
        'название',
        max_length=32,
        help_text='Максимум 32 символа',
    )
    description = models.TextField(
        'описание',
        max_length=200,
        help_text='Максимум 200 символов',
    )
    new_url = models.URLField(
        'ссылка на новость',
        max_length=128,
    )

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    @staticmethod
    def get_all_objects_by_id():
        return News.objects.order_by('-id')
