# Generated by Django 4.2.1 on 2023-05-25 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
