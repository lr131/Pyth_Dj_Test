# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fio', models.CharField(max_length=500)),
                ('bdata', models.DateField()),
                ('bilet', models.CharField(max_length=50)),
                ('cgrup', models.ForeignKey(to='grups.Grup')),
            ],
        ),
    ]
