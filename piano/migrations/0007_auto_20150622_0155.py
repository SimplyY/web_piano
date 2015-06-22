# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0006_auto_20150620_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piano',
            name='image_link',
            field=models.CharField(max_length=200),
        ),
    ]
