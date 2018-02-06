# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_original',
            field=models.ImageField(null=True, upload_to=b'photos/profile/original'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to=b'photos/profile/photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_thumbs',
            field=models.ImageField(null=True, upload_to=b'photos/profile/thumbs'),
        ),
    ]
