# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-17 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='point',
            name='long',
            field=models.FloatField(),
        ),
    ]