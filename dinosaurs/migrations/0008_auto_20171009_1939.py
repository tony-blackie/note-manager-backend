# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-09 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurs', '0007_note_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dinosaurs.Folder'),
        ),
    ]
