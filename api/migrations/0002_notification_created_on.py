# Generated by Django 3.2.4 on 2021-06-08 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 8, 11, 4, 37, 327057)),
        ),
    ]
