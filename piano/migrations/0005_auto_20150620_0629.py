# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('piano', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Piano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('info', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('use_time', models.CharField(max_length=20)),
                ('image_link', models.CharField(max_length=20)),
                ('seller', models.ForeignKey(to='piano.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='piano',
            field=models.ForeignKey(to='piano.Piano'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='piano.User'),
        ),
    ]
