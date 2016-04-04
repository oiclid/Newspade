# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysites', '0008_auto_20160402_2007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aljazeeranews',
            options={'ordering': ['-id'], 'verbose_name_plural': 'AljazeeraNews'},
        ),
        migrations.AlterModelOptions(
            name='bbcnews',
            options={'ordering': ['-id'], 'verbose_name_plural': 'BBCNews'},
        ),
        migrations.AlterModelOptions(
            name='reutersnews',
            options={'ordering': ['-id'], 'verbose_name_plural': 'ReutersNews'},
        ),
    ]
