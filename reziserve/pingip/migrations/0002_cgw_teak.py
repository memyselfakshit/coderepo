# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pingip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cgw',
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
            name='teak',
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
    ]
