# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-29 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profille', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='PostCode',
            field=models.IntegerField(default=0),
        ),
    ]