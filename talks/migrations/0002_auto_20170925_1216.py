# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizer',
            name='twitter',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='linkedin',
            field=models.URLField(null=True),
        ),
    ]
