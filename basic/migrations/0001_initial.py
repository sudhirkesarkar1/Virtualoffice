# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-07-07 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_US',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Query', models.TextField()),
                ('Contact_number', models.IntegerField()),
            ],
        ),
    ]