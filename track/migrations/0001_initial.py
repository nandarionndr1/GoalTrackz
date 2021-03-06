# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-01 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subtask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('task_desc', models.TextField()),
                ('goal_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='track.Goal')),
            ],
        ),
    ]
