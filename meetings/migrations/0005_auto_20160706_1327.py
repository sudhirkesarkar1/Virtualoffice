# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-07-06 07:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0004_auto_20160704_2106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meets',
            options={'ordering': ['-Meeting_Date']},
        ),
    ]