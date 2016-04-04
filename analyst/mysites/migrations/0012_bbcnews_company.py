# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysites', '0011_aljazeeranews_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbcnews',
            name='company',
            field=models.CharField(default='BBC News', max_length=100),
        ),
    ]
