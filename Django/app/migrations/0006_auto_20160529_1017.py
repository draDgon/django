# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160528_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='chapin',
            field=models.PositiveIntegerField(default=0, verbose_name='差评'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='dianzan',
            field=models.PositiveIntegerField(default=0, verbose_name='点赞'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='look',
            field=models.PositiveIntegerField(default=0, verbose_name='浏览量'),
        ),
    ]