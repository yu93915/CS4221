# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0002_auto_20170316_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_id', models.IntegerField()),
                ('i_im_id', models.CharField(max_length=20)),
                ('i_name', models.CharField(max_length=20)),
                ('i_price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
