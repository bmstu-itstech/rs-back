# Generated by Django 5.1.7 on 2025-03-12 15:07

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
                ('name', models.CharField(help_text='Название партнёрской организации', max_length=100, verbose_name='Название')),
                ('url', models.URLField(help_text='Ссылка на сайт партнёра', verbose_name='Ссылка')),
                ('logo', models.ImageField(help_text='Изображение логотипа партнёра', upload_to='partners', verbose_name='Логотип')),
            ],
        ),
    ]
