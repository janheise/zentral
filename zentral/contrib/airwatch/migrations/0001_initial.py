# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 14:01
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0020_machinesnapshotcommit_last_seen'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirwatchApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airwatch_id', models.IntegerField(verbose_name='Airwatch ID')),
                ('builder', models.CharField(max_length=256)),
                ('build_kwargs', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Builder parameters')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AirwatchInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(help_text='host name of the server', max_length=256)),
                ('port', models.IntegerField(default=8443, help_text='server port number',
                                             validators=[django.core.validators.MinValueValidator(1),
                                                         django.core.validators.MaxValueValidator(65535)])),
                ('path', models.CharField(default='/JSSResource', help_text='path of the server API', max_length=64)),
                ('user', models.CharField(help_text='API user name', max_length=64)),
                ('password', models.CharField(help_text='API user password', max_length=256)),
                ('aw_tenant_code', models.CharField(help_text='Airwatch tenant code', max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.BusinessUnit')),
            ],
        ),
        migrations.AddField(
            model_name='airwatchapp',
            name='airwatch_instance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airwatch.AirwatchInstance'),
        ),
    ]
