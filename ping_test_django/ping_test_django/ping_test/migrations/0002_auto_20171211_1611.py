# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ping_test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serveriplist',
            name='Lost',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='serveriplist',
            name='Recieved',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='serveriplist',
            name='Sent',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
