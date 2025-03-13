from django.db import models


class NewsRecord(models.Model):
    title = models.CharField(
        'Заголовок',
        max_length=100,
        help_text='Заголовок, краткое описание новости. Не более 100 символов',
    )
    content = models.TextField(
        'Содержание',
        help_text='Текст новости',
    )
    href = models.URLField(
        'Ссылка',
        help_text='Ссылка на пост в соцсетях с более подробной информацией о новости'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='news/',
        help_text='Изображение для новости'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
