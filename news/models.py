from django.db import models


class NewsRecord(models.Model):
    """
    Новость, связанная с ЦМР, публикуемая на сайте.
    """
    title = models.CharField(
        max_length=100,
        help_text='Заголовок, краткое описание новости. Не более 100 символов',
    )
    content = models.TextField(
        help_text='Текст новости',
    )
    href = models.URLField(
        help_text='Ссылка на пост в соцсетях с более подробной информацией о новости'
    )
    image = models.ImageField(
        upload_to='news/',
        help_text='Изображение для новости'
    )
