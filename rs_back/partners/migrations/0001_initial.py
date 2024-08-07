# Generated by Django 4.2.6 on 2024-07-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='изображение к мероприятию')),
                ('title', models.CharField(help_text='Максимум 150 символов', max_length=150, verbose_name='название')),
                ('link', models.URLField(verbose_name='ссылка на сайт')),
            ],
            options={
                'verbose_name': 'партнёр',
                'verbose_name_plural': 'партнёры',
            },
        ),
    ]
