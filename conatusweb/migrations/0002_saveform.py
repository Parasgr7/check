# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-12 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conatusweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('student_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]
