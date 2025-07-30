from django.db import models


class NewsRecord(models.Model):
    title = models.TextField(
        'Заголовок',
        help_text='Заголовок, краткое описание новости',
    )
    content = models.TextField(
        'Содержание',
        blank=True,
        help_text='Текст новости',
    )
    href = models.URLField(
        'Ссылка',
        blank=True,
        help_text='Ссылка на пост в соцсетях с более подробной информацией'
    )
    image = models.ImageField(
        'Изображение',
        blank=True,
        null=True,
        upload_to='news/',
        help_text='Изображение для новости'
    )

    def __str__(self):
        return f"{self.title} ({self.href})" if self.href else self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
