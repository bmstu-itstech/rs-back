from django.db import models


class Partner(models.Model):
    name = models.CharField(
        'Название',
        max_length=100,
        help_text='Название партнёрской организации',
    )
    url = models.URLField(
        'Ссылка',
        help_text='Ссылка на сайт партнёра',
    )
    logo = models.ImageField(
        'Логотип',
        upload_to='partners',
        help_text='Изображение логотипа партнёра',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
