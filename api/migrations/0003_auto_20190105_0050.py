# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-04 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190105_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='join_date',
            field=models.DateTimeField(),
        ),
    ]
