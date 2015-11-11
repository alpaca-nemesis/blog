# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0002_auto_20151110_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='content',
            field=models.TextField(default='null', verbose_name='content'),
            preserve_default=False,
        ),
    ]
