from django.db import models


class Achievement(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        help_text='Заголовок, краткое описание достижения. Не более 100 символов',
    )
    description = models.TextField(
        'Описание',
        help_text='Описание достижения ЦМР'
    )
    album_url = models.URLField(
        'Альбом',
        help_text='Ссылка на фотоальбом в соцсетях или на сайте',
    )
    media_url = models.URLField(
        'СМИ',
        help_text='Ссылка на упоминание в соцсетях',
    )
    image = models.ImageField(
        'Изображение',
        null=True,
        upload_to='achievements',
        help_text='Фотография с мероприятия',
    )

    def __str__(self):
        return self.title
