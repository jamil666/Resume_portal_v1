# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0016_auto_20170228_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Date_1',
            new_name='Date_01',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Date_2',
            new_name='Date_02',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Date_3',
            new_name='Date_03',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Date_4',
            new_name='Date_04',
        ),
    ]