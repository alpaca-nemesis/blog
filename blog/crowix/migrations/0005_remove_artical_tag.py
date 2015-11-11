# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0004_artical_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artical',
            name='tag',
        ),
    ]
