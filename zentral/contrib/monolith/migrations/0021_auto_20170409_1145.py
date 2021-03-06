# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-09 11:45
from __future__ import unicode_literals

from django.db import migrations
from zentral.contrib.monolith.conf import monolith_conf
from zentral.contrib.monolith.models import ManifestEnrollmentPackage
from zentral.contrib.monolith.utils import build_manifest_enrollment_package


def create_manifest_enrollment_packages(apps, schema_editor):
    MigrationManifest = apps.get_model("monolith", "Manifest")
    MigrationManifestEnrollmentPackage = apps.get_model("monolith", "ManifestEnrollmentPackage")
    for manifest in MigrationManifest.objects.all():
        for builder, builder_config in monolith_conf.enrollment_package_builders.items():
            if not builder_config["optional"] \
               or "contrib.santa" in builder and manifest.zentral_santa \
               or "contrib.osquery" in builder and manifest.zentral_osquery:
                print("Creating mep {} for manifest {}".format(builder, manifest))
                mep, _ = MigrationManifestEnrollmentPackage.objects.get_or_create(
                    manifest=manifest,
                    builder=builder,
                    defaults={"build_kwargs": {},
                              "version": 1}
                )
                mep.refresh_from_db()


def build_manifest_enrollment_packages(apps, schema_editor):
    for mep in ManifestEnrollmentPackage.objects.all():
        build_manifest_enrollment_package(mep)


class Migration(migrations.Migration):

    dependencies = [
        ('monolith', '0020_auto_20170409_1014'),
    ]

    operations = [
        migrations.RunPython(create_manifest_enrollment_packages),
        migrations.RunPython(build_manifest_enrollment_packages),
    ]
