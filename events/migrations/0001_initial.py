# Generated by Django 5.1.7 on 2025-03-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название мероприятия, например, Хардатон Инженерный Вызов. Не более 100 символов', max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, help_text='Подробное описание мероприятия', verbose_name='Описание')),
                ('date', models.CharField(help_text='Дата проведения мероприятия, например, 31.02.25', max_length=50, null=True, verbose_name='Дата')),
                ('media_url', models.URLField(blank=True, help_text='Ссылка на упоминание в соцсетях', verbose_name='СМИ')),
                ('album_url', models.URLField(blank=True, help_text='Ссылка на фотоальбом в соцсетях или на сайте', verbose_name='Альбом')),
                ('on_map_url', models.URLField(blank=True, help_text='Ссылка на место проведения мероприятия в приложение (например, Яндекс Карты)', verbose_name='Место')),
                ('docs_url', models.URLField(blank=True, help_text='Ссылка на нормативные документы, регламентирующие проведение мероприятия', verbose_name='Документы')),
            ],
        ),
    ]
