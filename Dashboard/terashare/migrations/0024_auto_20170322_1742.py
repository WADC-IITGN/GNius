# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 12:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0023_file_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Sunday',
            new_name='Sun',
        ),
    ]