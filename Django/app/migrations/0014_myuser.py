# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True, verbose_name='Email')),
                ('username', models.CharField(db_index=True, max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('type', models.IntegerField(default=0)),
                ('sex', models.IntegerField(default=1)),
                ('uid', models.CharField(max_length=50, null=True)),
                ('access_token', models.CharField(max_length=100, null=True)),
                ('url', models.URLField(null=True)),
                ('desc', models.CharField(max_length=2000, null=True)),
                ('avatar', models.CharField(max_length=500, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
