from django.db import models


class HardathonPreview(models.Model):
    href = models.TextField(
        'Ссылка',
        blank=True,
    )
    title = models.TextField(
        'Название',
        blank=True,
    )
    photo = models.TextField(
        'Изображение',
        blank=True,
    )

    class Meta:
        verbose_name = 'Предварительный просмотр хардaтона'
        verbose_name_plural = 'Предварительные просмотры хардaтонов'
