# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-06 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0003_remove_subtask_task_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]