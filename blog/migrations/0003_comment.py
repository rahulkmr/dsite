# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161219_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commenter', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Commented on')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Entry')),
            ],
        ),
    ]
