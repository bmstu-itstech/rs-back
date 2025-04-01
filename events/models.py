from django.db import models


class Event(models.Model):
    name = models.CharField(
        'Название',
        max_length=100,
        help_text='Название мероприятия, например, Хардатон Инженерный Вызов. Не более 100 символов',
    )
    description = models.TextField(
        'Описание',
        blank=True,
        help_text='Подробное описание мероприятия',
    )
    date = models.CharField(
        'Дата',
        null=True,
        max_length=50,
        help_text='Дата проведения мероприятия, например, 31.02.25',
    )
    media_url = models.URLField(
        'СМИ',
        blank=True,
        help_text='Ссылка на упоминание в соцсетях',
    )
    album_url = models.URLField(
        'Альбом',
        blank=True,
        help_text='Ссылка на фотоальбом в соцсетях или на сайте',
    )
    on_map_url = models.URLField(
        'Место',
        blank=True,
        help_text='Ссылка на место проведения мероприятия в приложение (например, Яндекс Карты)',
    )
    docs_url = models.URLField(
        'Документы',
        blank=True,
        help_text='Ссылка на нормативные документы, регламентирующие проведение мероприятия',
    )
    background_img = models.ImageField(
        'Изображение',
        blank=True,
        null=True,
        upload_to='events/backgrounds/',
        help_text='Фоновое изображение для мероприятия'
    )

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
