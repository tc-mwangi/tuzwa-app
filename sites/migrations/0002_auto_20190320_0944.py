# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 06:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='rating',
            name='overall_score',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20),
        ),
    ]
