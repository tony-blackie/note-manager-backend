# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurs', '0019_auto_20180113_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='hashtags',
        ),
        migrations.AddField(
            model_name='note',
            name='hashtag',
            field=models.ManyToManyField(blank=True, null=True, to='dinosaurs.Hashtag'),
        ),
    ]
