from django.db import models


class Hardathon(models.Model):
    title = models.TextField(
        'Название',
        help_text='Название мероприятия, например, Хардатон Инженерный Вызов',
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
    date = models.DateField(
        'Дата проведения',
        blank=True,
        null=True,
        help_text='Дата проведения',
    )
    start_date = models.DateField(
        'Старт приёма заявок',
        blank=True,
        null=True,
        help_text='Дата старта приёма заявок',
    )
    end_date = models.DateField(
        'Окончание регистрации',
        blank=True,
        null=True,
        help_text='Дата окончания регистрации',
    )
    result_date = models.DateField(
        'Итоги',
        blank=True,
        null=True,
        help_text='Дата подведения итогов',
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

    def __str__(self):
        return f"{self.title} ({self.href})" if self.href else self.title

    class Meta:
        verbose_name = 'Хардатон'
        verbose_name_plural = 'Хардатоны'
