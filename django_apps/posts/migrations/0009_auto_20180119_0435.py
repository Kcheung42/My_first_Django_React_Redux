# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-19 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20180119_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field='img_height', null=True, upload_to='', width_field='img_width'),
        ),
        migrations.AddField(
            model_name='post',
            name='img_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='img_width',
            field=models.IntegerField(default=0),
        ),
    ]
