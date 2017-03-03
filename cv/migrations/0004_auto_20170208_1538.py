# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20170208_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Lang2',
            new_name='Language1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Lang3',
            new_name='Language2',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Lang4',
            new_name='Language3',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Lang5',
            new_name='Language4',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Lang1',
        ),
        migrations.AddField(
            model_name='profile',
            name='Language1_Quality',
            field=models.CharField(blank=True, choices=[('Fluent', 'Fluent'), ('Good', 'Good'), ('Bad', 'Bad')], max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='Language2_Quality',
            field=models.CharField(blank=True, choices=[('Fluent', 'Fluent'), ('Good', 'Good'), ('Bad', 'Bad')], max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='Language3_Quality',
            field=models.CharField(blank=True, choices=[('Fluent', 'Fluent'), ('Good', 'Good'), ('Bad', 'Bad')], max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='Language4_Quality',
            field=models.CharField(blank=True, choices=[('Fluent', 'Fluent'), ('Good', 'Good'), ('Bad', 'Bad')], max_length=255),
        ),
        migrations.AddField(
            model_name='profile',
            name='Language5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='Language5_Quality',
            field=models.CharField(blank=True, choices=[('Fluent', 'Fluent'), ('Good', 'Good'), ('Bad', 'Bad')], max_length=255),
        ),
    ]