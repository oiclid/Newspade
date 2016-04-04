# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160310_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='jobtitle',
            field=models.CharField(max_length=140, null=True, verbose_name=b'Job Title', blank=True),
        ),
    ]
