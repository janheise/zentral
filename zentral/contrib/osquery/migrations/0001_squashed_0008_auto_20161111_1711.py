# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 16:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# zentral.contrib.osquery.migrations.0007_auto_20161111_0204

class Migration(migrations.Migration):

    replaces = [('osquery', '0001_initial'), ('osquery', '0002_delete_node'), ('osquery', '0003_auto_20160207_1524'), ('osquery', '0004_distributedquery_tags'), ('osquery', '0005_auto_20160512_1718'), ('osquery', '0006_distributedqueryprobemachine'), ('osquery', '0007_auto_20161111_0204'), ('osquery', '0008_auto_20161111_1711')]

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('inventory', '0004_auto_20160505_0639'),
        ('probes', '0007_auto_20161105_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributedQueryProbeMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_serial_number', models.CharField(db_index=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('probe_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='probes.ProbeSource')),
            ],
        ),
    ]
