# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-29 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profille', '0002_auto_20160629_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='Virtual_Office_Location',
            field=models.CharField(choices=[('Andheri', 'Andheri'), ('Borivali', 'Borivali'), ('Miraroad', 'Miraroad'), ('Virar', 'Virar')], max_length=15),
        ),
    ]
