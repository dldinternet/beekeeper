# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-21 00:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws', '0012_rename_pending'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='spot',
            field=models.BooleanField(default=False),
        ),
    ]
