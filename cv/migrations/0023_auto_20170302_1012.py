# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0022_auto_20170302_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Photo',
            field=models.FileField(blank=True, upload_to='C:\\Django\\cv_portal\\cv/static/images/profile_photos/'),
        ),
    ]