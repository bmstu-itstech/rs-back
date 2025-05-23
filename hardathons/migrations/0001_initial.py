# Generated by Django 5.1.7 on 2025-05-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hardathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название мероприятия, например, Хардатон Инженерный Вызов. Не более 100 символов', max_length=100, verbose_name='Название')),
                ('href', models.URLField(blank=True, help_text='Ссылка на хардатон', verbose_name='Ссылка')),
                ('background_image', models.ImageField(blank=True, null=True, upload_to='hardathon/backgrounds/', verbose_name='Фоновое изображение')),
                ('date', models.CharField(blank=True, help_text='Дата проведения, например, 11.05.2025', max_length=100, verbose_name='Дата проведения')),
                ('start_date', models.CharField(blank=True, help_text='Дата старта приёма заявок, например, 11.05.2025', max_length=100, verbose_name='Старт приёма заявок')),
                ('end_date', models.CharField(blank=True, help_text='Дата окончания регистрации, например, 11.05.2025', max_length=100, verbose_name='Окончание регистрации')),
                ('result_date', models.CharField(blank=True, help_text='Дата подведения итогов, например, 11.05.2025', max_length=100, verbose_name='Итоги')),
                ('place', models.TextField(blank=True, help_text='Месторо проведения (адрес/ссылка)', verbose_name='Место проведения')),
                ('media', models.TextField(blank=True, help_text='Упоминания в СМИ', verbose_name='СМИ')),
                ('projects', models.TextField(blank=True, verbose_name='Проекты')),
                ('images', models.TextField(blank=True, verbose_name='Фото')),
                ('documents', models.TextField(blank=True, verbose_name='Документы')),
                ('partners', models.TextField(blank=True, verbose_name='Партнёры')),
            ],
            options={
                'verbose_name': 'Хардатон',
                'verbose_name_plural': 'Хардатоны',
            },
        ),
    ]
