# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0005_remove_artical_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='tag',
            field=models.CharField(default='tag', max_length=20, verbose_name='tag'),
            preserve_default=False,
        ),
    ]
