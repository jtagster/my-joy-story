# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-12 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170802_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='emotionTags',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='gratitudeStmt',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='sensationTags',
            field=models.CharField(max_length=500),
        ),
    ]
