from django.db import models


class Hardathon(models.Model):
    title = models.CharField(
        'Название',
        max_length=100,
        help_text='Название мероприятия, например, Хардатон Инженерный Вызов. Не более 100 символов',
    )
    href = models.URLField(
        'Ссылка',
        blank=True,
        help_text='Ссылка на хардатон',
    )
    background_image = models.ImageField(
        'Фоновое изображение',
        blank=True,
        null=True,
        upload_to='hardathon/backgrounds/',
    )
    quote = models.TextField(
        'Цитата',
        blank=True,
    )
    date = models.CharField(
        'Дата проведения',
        blank=True,
        max_length=100,
        help_text='Дата проведения, например, 11.05.2025',
    )
    start_date = models.CharField(
        'Старт приёма заявок',
        blank=True,
        max_length=100,
        help_text='Дата старта приёма заявок, например, 11.05.2025',
    )
    end_date = models.CharField(
        'Окончание регистрации',
        blank=True,
        max_length=100,
        help_text='Дата окончания регистрации, например, 11.05.2025',
    )
    result_date = models.CharField(
        'Итоги',
        blank=True,
        max_length=100,
        help_text='Дата подведения итогов, например, 11.05.2025',
    )
    place = models.TextField(
        'Место проведения',
        blank=True,
        help_text='Место проведения (адрес/ссылка)',
    )
    media = models.TextField(
        'СМИ',
        blank=True,
        help_text='Упоминания в СМИ',
    )
    projects = models.TextField(
        'Проекты',
        blank=True,
    )
    images = models.TextField(
        'Фото',
        blank=True,
    )
    documents = models.TextField(
        'Документы',
        blank=True,
    )
    partners = models.TextField(
        'Партнёры',
        blank=True,
    )

    class Meta:
        verbose_name = 'Хардатон'
        verbose_name_plural = 'Хардатоны'
