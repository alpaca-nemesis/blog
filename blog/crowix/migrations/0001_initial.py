# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=80, verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('tag', models.CharField(max_length=20, verbose_name='tag')),
                ('slug', models.CharField(max_length=256, verbose_name='slug', db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('mail', models.CharField(max_length=30, verbose_name='mail')),
                ('phone', models.CharField(max_length=30, verbose_name='phone')),
                ('content', models.TextField(verbose_name='content')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
