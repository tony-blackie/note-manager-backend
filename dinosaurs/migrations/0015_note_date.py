# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurs', '0014_remove_note_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
