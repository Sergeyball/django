# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-15 09:45
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170518_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(), upload_to=b'logotypes/%Y%m%d', verbose_name='logotype'),
        ),
    ]
