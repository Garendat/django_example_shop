# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-05 20:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20180606_0150'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productinbasket',
            old_name='products',
            new_name='product',
        ),
    ]
