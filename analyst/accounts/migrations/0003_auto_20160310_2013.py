# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160310_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='googleplus',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(null=True, blank=True),
        ),
    ]
