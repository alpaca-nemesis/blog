# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0002_auto_20151120_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='mail',
            field=models.CharField(max_length=30, verbose_name='mail'),
            preserve_default=True,
        ),
    ]
