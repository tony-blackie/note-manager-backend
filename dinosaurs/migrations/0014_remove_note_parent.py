# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 22:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurs', '0013_auto_20171104_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='parent',
        ),
    ]
