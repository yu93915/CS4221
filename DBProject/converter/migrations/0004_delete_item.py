# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_auto_20170316_1626'),
    ]

    operations = [
        migrations.DeleteModel(
            name='item',
        ),
    ]