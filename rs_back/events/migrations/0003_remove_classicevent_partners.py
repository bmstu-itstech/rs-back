# Generated by Django 4.2.6 on 2024-08-11 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_seacher_vk_questionnaire_searcher_vk_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classicevent',
            name='partners',
        ),
    ]