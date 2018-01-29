# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.TextField(default=datetime.datetime(2018, 1, 28, 16, 57, 45, 999505, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
