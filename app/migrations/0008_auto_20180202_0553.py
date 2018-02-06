# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180202_0425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile_pic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_original', models.ImageField(upload_to=b'photos/profile/original', blank=True)),
                ('profile_thumbs', models.ImageField(upload_to=b'photos/profile/thumbs', blank=True)),
                ('profile_photo', models.ImageField(upload_to=b'photos/profile/photo', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_original',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_photo',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_thumbs',
        ),
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile_pic',
            name='profile',
            field=models.OneToOneField(to='app.Profile'),
        ),
    ]
