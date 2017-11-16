# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-16 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0044_auto_20171116_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groundtruthannotation',
            name='algorithm',
        ),
        migrations.RemoveField(
            model_name='groundtruthannotation',
            name='type',
        ),
        migrations.AddField(
            model_name='groundtruthannotation',
            name='from_propagation',
            field=models.BooleanField(default=False),
        ),
    ]
