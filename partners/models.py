from django.db import models


class Partner(models.Model):
    name = models.TextField(
        'Название',
        help_text='Название партнёрской организации',
    )
    url = models.URLField(
        'Ссылка',
        blank=True,
        help_text='Ссылка на сайт партнёра',
    )
    logo = models.ImageField(
        'Логотип',
        blank=True,
        null=True,
        upload_to='partners/',
        help_text='Изображение логотипа партнёра',
    )

    def __str__(self):
        return f"{self.name} ({self.url})" if self.url else self.name

    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'
