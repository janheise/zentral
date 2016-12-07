# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 16:55
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


# Functions from the following migrations need manual copying.
# Move them and any dependencies into this file, then update the
# RunPython operations to refer to the local versions:
# zentral.core.probes.migrations.0004_auto_20161103_1728
# zentral.core.probes.migrations.0006_auto_20161104_1343
# zentral.core.probes.migrations.0008_auto_20161111_1906
# zentral.core.probes.migrations.0009_auto_20161127_1928
# zentral.core.probes.migrations.0010_auto_20161129_1733

class Migration(migrations.Migration):

    replaces = [('probes', '0001_initial'), ('probes', '0002_auto_20160602_1001'), ('probes', '0003_auto_20160604_0908'), ('probes', '0004_auto_20161103_1728'), ('probes', '0005_auto_20161104_1343'), ('probes', '0006_auto_20161104_1343'), ('probes', '0007_auto_20161105_1647'), ('probes', '0008_auto_20161111_1906'), ('probes', '0009_auto_20161127_1928'), ('probes', '0010_auto_20161129_1733')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProbeSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE', max_length=32)),
                ('description', models.TextField(blank=True)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='probesource',
            options={'ordering': ('name', 'id')},
        ),
        migrations.AlterField(
            model_name='probesource',
            name='body',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='probesource',
            name='apps',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=[], editable=False, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='probesource',
            name='event_types',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=[], editable=False, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='probesource',
            name='model',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='probesource',
            name='body',
            field=models.TextField(editable=False),
        ),
        migrations.AlterField(
            model_name='probesource',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='probesource',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='INACTIVE', max_length=32),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedImport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('OK', 'OK'), ('DOWNLOAD_ERROR', 'download error'), ('FEED_ERROR', 'feed error')], max_length=32)),
                ('new_probes', models.PositiveIntegerField(default=0)),
                ('updated_probes', models.PositiveIntegerField(default=0)),
                ('archived_probes', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='probes.Feed')),
            ],
        ),
        migrations.CreateModel(
            name='FeedProbe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('key', models.CharField(max_length=255)),
                ('body', django.contrib.postgres.fields.jsonb.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('archived_at', models.DateTimeField(blank=True, null=True)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='probes.Feed')),
            ],
        ),
        migrations.RemoveField(
            model_name='probesource',
            name='apps',
        ),
        migrations.AlterField(
            model_name='probesource',
            name='body',
            field=django.contrib.postgres.fields.jsonb.JSONField(editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='feedprobe',
            unique_together=set([('feed', 'key')]),
        ),
    ]
