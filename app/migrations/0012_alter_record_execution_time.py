# Generated by Django 4.1.7 on 2023-03-05 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_record_execution_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='execution_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 22, 32, 3, 750744)),
        ),
    ]
