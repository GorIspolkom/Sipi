# Generated by Django 4.1.7 on 2023-03-01 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_policy_policy_path_policy_inventory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='inventory',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='policy',
            name='playbook_path',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='record',
            name='execution_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 22, 57, 32, 107606)),
        ),
    ]
