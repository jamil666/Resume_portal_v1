# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0027_auto_20170302_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Photo',
            field=models.FileField(blank=True, upload_to='cv/static/images/profile_photos/', verbose_name='static/images/profile_photos/'),
        ),
    ]
