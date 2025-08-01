# Generated by Django 5.2.1 on 2025-07-28 09:39

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
                ('name', models.TextField(help_text='Название партнёрской организации', verbose_name='Название')),
                ('url', models.URLField(blank=True, help_text='Ссылка на сайт партнёра', verbose_name='Ссылка')),
                ('logo', models.ImageField(blank=True, help_text='Изображение логотипа партнёра', null=True, upload_to='partners/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёры',
            },
        ),
    ]
