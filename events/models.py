from django.db import models


class Event(models.Model):
    name = models.TextField(
        'Название',
        help_text='Название мероприятия, например, Хардатон Инженерный Вызов',
    )
    description = models.TextField(
        'Описание',
        blank=True,
        help_text='Подробное описание мероприятия',
    )
    date = models.DateField(
        'Дата',
        blank=True,
        null=True,
        help_text='Дата проведения мероприятия',
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
    registration_url = models.URLField(
        'Регистрация',
        blank=True,
        help_text='Ссылка на регистрацию на событие',
    )
    background_img = models.ImageField(
        'Изображение',
        blank=True,
        null=True,
        upload_to='events/backgrounds/',
        help_text='Фоновое изображение для мероприятия',
    )

    def __str__(self):
        return f"{self.name} ({self.date})" if self.date else self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
