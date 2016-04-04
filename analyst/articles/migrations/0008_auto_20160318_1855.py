# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20160318_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tldr',
            field=markdownx.models.MarkdownxField(null=True, verbose_name=b'TLDR;', blank=True),
        ),
    ]
