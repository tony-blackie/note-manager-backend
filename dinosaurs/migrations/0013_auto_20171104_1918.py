# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurs', '0012_auto_20171104_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='is_root',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='folder',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='dinosaurs.Person'),
        ),
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='dinosaurs.Person'),
        ),
        migrations.AlterField(
            model_name='note',
            name='folder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='dinosaurs.Folder'),
        ),
    ]
