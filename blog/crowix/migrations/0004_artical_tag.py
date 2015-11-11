# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crowix', '0003_artical_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='artical',
            name='tag',
            field=models.CharField(default=datetime.datetime(2015, 11, 10, 8, 42, 3, 795328, tzinfo=utc), max_length=50, verbose_name='tag'),
            preserve_default=False,
        ),
    ]
