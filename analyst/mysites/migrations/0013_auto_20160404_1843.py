# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0017_added_order_to_scraped_obj_attr'),
        ('mysites', '0012_bbcnews_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticoNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('company', models.CharField(default='Politico', max_length=100)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name_plural': 'Politico News',
            },
        ),
        migrations.CreateModel(
            name='PoliticoWebsite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('head', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.Scraper', null=True)),
                ('scraper_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='politiconews',
            name='news_website',
            field=models.ForeignKey(to='mysites.PoliticoWebsite'),
        ),
    ]
