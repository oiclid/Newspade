# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=18, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(max_length=140, null=True, verbose_name=b'First Name', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(max_length=140, null=True, verbose_name=b'Last Name', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'media/profile', blank=True),
        ),
    ]
