# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0015_auto_20170228_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Photo',
            field=models.ImageField(blank=True, upload_to='/static/images/'),
        ),
    ]