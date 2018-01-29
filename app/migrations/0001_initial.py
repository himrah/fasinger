# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_time', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('comment', models.TextField()),
                ('comment_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_photo', models.ImageField(upload_to=b'photos/original')),
                ('thumbs', models.ImageField(upload_to=b'photos/thumbs/')),
                ('photo', models.ImageField(upload_to=b'photos/photo')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('comment', models.TextField()),
                ('upload_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='photo_id',
            field=models.ForeignKey(to='app.Photos', null=True),
        ),
    ]
