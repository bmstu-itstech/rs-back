# Generated by Django 4.2.6 on 2024-08-11 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(help_text='Максимум 200 символов', max_length=200, verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='new_url',
            field=models.URLField(max_length=128, verbose_name='ссылка на новость'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(help_text='Максимум 32 символа', max_length=32, verbose_name='название'),
        ),
    ]
