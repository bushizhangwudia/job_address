# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flame', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='urltype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlname', models.CharField(max_length=30, verbose_name='网址类型')),
                ('nick', models.CharField(max_length=10, verbose_name='昵称')),
            ],
            options={
                'verbose_name_plural': '网址类型',
            },
        ),
    ]
