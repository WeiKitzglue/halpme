# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-17 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findme', '0002_auto_20170916_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='point',
            old_name='long',
            new_name='lon',
        ),
        migrations.AddField(
            model_name='point',
            name='phone_no',
            field=models.CharField(default=1234567890, max_length=12),
            preserve_default=False,
        ),
    ]
