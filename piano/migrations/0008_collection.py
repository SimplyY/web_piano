# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0007_auto_20150622_0155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('piano', models.ForeignKey(to='piano.Piano')),
                ('user', models.ForeignKey(to='piano.User')),
            ],
        ),
    ]
