# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cementerio', '0005_auto_20170901_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimiento',
            name='abono',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='cargo',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
