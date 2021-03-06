# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-07-31 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurs', '0004_folder_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='folder',
            name='parent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='parent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='text',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]
