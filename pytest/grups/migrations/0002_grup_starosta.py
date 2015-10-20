# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('grups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grup',
            name='starosta',
            field=models.ForeignKey(to='students.Student'),
        ),
    ]
