# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160310_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(null=True, verbose_name=b'Facebook', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='googleplus',
            field=models.URLField(null=True, verbose_name=b'Google +', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(null=True, verbose_name=b'LinkedIn', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(null=True, verbose_name=b'Twitter', blank=True),
        ),
    ]
