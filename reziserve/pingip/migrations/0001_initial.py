# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='m3servers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(max_length=50)),
                ('Domain', models.CharField(max_length=150)),
                ('Hostname', models.CharField(max_length=150)),
                ('Location', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Latitude', models.CharField(max_length=50)),
                ('Longitude', models.CharField(max_length=50)),
                ('Division', models.CharField(max_length=50)),
                ('Region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='serversm3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP', models.CharField(max_length=50)),
                ('Domain', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='states',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Abbr', models.CharField(max_length=50)),
            ],
        ),
    ]
