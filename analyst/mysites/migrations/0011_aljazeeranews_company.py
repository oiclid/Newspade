# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysites', '0010_reutersnews_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='aljazeeranews',
            name='company',
            field=models.CharField(default='Aljazeera', max_length=100),
        ),
    ]
