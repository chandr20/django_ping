# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ping_test', '0002_auto_20171211_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='PingJobuid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PingGuid', models.CharField(max_length=120)),
                ('State', models.CharField(default='started', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='serveriplist',
            name='Ping_Job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ping_test.PingJobuid'),
        ),
    ]