# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-17 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161218_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]