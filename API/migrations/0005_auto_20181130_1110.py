# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-11-30 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20181130_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='icp_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='output',
            name='icp_id',
            field=models.IntegerField(),
        ),
    ]
