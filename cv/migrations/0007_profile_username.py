# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20170208_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='UserName',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]