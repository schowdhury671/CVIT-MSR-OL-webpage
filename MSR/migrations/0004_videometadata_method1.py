# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSR', '0003_remove_videometadata_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='videometadata',
            name='method1',
            field=models.IntegerField(default='0'),
        ),
    ]
