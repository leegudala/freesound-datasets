# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-07 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0027_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='is_trustable',
            field=models.NullBooleanField(),
        ),
    ]