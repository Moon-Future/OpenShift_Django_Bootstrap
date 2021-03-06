# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 15:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('PhoneNum', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number \n\t\tmust be entered in the format: 13588888888. Up to 11 digits allowed. ', regex='^\\d{11}$')])),
                ('UpdateTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('Address', models.TextField(blank=True)),
                ('Other', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-UpdateTime'],
            },
        ),
    ]
