# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20170811_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]