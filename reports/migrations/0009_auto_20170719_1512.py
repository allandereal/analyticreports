# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20170719_0026'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['name']},
        ),
    ]