# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='tldr',
            field=markdownx.models.MarkdownxField(default='deffy'),
            preserve_default=False,
        ),
    ]
