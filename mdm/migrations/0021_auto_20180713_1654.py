# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-13 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0020_auto_20180713_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job_data',
            old_name='parent_pos_key',
            new_name='pos_key',
        ),
    ]