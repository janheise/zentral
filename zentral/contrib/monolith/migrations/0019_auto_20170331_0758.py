# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monolith', '0018_auto_20170331_0731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submanifestattachment',
            name='identifier',
            field=models.TextField(blank=True, null=True),
        ),
    ]
