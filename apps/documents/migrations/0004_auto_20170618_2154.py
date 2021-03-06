# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-18 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20170410_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audittrail',
            name='type',
            field=models.PositiveIntegerField(choices=[(1, 'agenda'), (2, 'minutes'), (4, 'board_book'), (3, 'other')], default=3, verbose_name='document type'),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.PositiveIntegerField(choices=[(1, 'agenda'), (2, 'minutes'), (4, 'board_book'), (3, 'other')], default=3, verbose_name='document type'),
        ),
    ]
