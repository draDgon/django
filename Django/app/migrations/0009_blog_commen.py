# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160529_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='commen',
            field=models.PositiveIntegerField(default=0, verbose_name='评论'),
        ),
    ]