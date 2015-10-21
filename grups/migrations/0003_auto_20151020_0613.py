# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grups', '0002_grup_starosta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grup',
            name='starosta',
            field=models.ForeignKey(blank=True, null=True, to='students.Student'),
        ),
    ]
