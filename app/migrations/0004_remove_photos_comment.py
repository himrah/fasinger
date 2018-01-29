# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_comments_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='comment',
        ),
    ]
