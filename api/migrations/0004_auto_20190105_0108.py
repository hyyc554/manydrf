# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-04 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190105_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='join_date',
            field=models.CharField(max_length=32),
        ),
    ]
