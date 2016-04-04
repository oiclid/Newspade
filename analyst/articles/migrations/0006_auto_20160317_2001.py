# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20160317_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=markdownx.models.MarkdownxField(max_length=100000),
        ),
    ]
