# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner_rotator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertiser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Advertiser',
                'verbose_name_plural': 'Advertisers',
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='advertiser',
            field=models.ForeignKey(verbose_name='Advertiser', blank=True, to='banner_rotator.Advertiser', null=True),
        ),
    ]
