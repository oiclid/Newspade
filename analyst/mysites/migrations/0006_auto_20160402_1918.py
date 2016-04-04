# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysites', '0005_auto_20160402_1907'),
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
