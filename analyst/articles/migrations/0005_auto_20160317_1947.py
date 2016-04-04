# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_articles_tldr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tldr',
            field=markdownx.models.MarkdownxField(null=True, blank=True),
        ),
    ]
