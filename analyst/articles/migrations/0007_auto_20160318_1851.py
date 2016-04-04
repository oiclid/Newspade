# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20160317_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tldr',
            field=markdownx.models.MarkdownxField(help_text=b'Too Long Didnt Read', null=True, verbose_name=b'TLDR;', blank=True),
        ),
    ]
