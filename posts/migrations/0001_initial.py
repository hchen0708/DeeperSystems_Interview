# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=500)),
                ('content', models.CharField(blank=True, max_length=5000, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]