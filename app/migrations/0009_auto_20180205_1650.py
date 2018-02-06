# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20180202_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='photo_id',
            field=models.ForeignKey(related_name='comments', to='app.Photos', null=True),
        ),
        migrations.AlterField(
            model_name='profile_pic',
            name='profile_original',
            field=models.ImageField(upload_to=b'photos/profile/original'),
        ),
        migrations.AlterField(
            model_name='profile_pic',
            name='profile_photo',
            field=models.ImageField(upload_to=b'photos/profile/photo'),
        ),
        migrations.AlterField(
            model_name='profile_pic',
            name='profile_thumbs',
            field=models.ImageField(upload_to=b'photos/profile/thumbs'),
        ),
    ]
