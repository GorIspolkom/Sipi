# Generated by Django 4.1.7 on 2023-03-05 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_policy_inventory_alter_policy_playbook_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='execution_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 21, 52, 9, 3206)),
        ),
    ]
