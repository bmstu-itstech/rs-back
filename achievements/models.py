from django.db import models


class Achievement(models.Model):
    title = models.TextField(
        'Заголовок',
        help_text='Заголовок, краткое описание достижения',
    )
    description = models.TextField(
        'Описание',
        blank=True,
        help_text='Описание достижения ЦМР'
    )
    album_url = models.URLField(
        'Альбом',
        blank=True,
        help_text='Ссылка на фотоальбом в соцсетях или на сайте',
    )
    media_url = models.URLField(
        'СМИ',
        blank=True,
        help_text='Ссылка на упоминание в соцсетях',
    )
    image = models.ImageField(
        'Изображение',
        blank=True,
        null=True,
        upload_to='achievements/',
        help_text='Фотография с мероприятия',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Достижение'
        verbose_name_plural = 'Достижения'
