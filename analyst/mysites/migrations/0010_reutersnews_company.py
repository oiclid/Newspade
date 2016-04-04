# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysites', '0009_auto_20160402_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='reutersnews',
            name='company',
            field=models.CharField(default='Reuters', max_length=100),
        ),
    ]
