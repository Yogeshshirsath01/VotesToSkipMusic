# Generated by Django 3.1.5 on 2021-01-25 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_merge_20210125_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='current_song',
        ),
    ]
