# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0005_auto_20150620_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piano',
            name='title',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
