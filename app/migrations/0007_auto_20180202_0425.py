# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180202_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_original',
            field=models.ImageField(default=datetime.datetime(2018, 2, 2, 4, 25, 19, 188468, tzinfo=utc), upload_to=b'photos/profile/original', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default=datetime.datetime(2018, 2, 2, 4, 25, 26, 476577, tzinfo=utc), upload_to=b'photos/profile/photo', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_thumbs',
            field=models.ImageField(upload_to=b'photos/profile/thumbs', blank=True),
        ),
    ]
