# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0017_added_order_to_scraped_obj_attr'),
        ('mysites', '0006_auto_20160402_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='AljazeeraAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
                ('news_website', models.ForeignKey(to='mysites.AljazeeraWebsite')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='NewsAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
                ('news_website', models.ForeignKey(to='mysites.NewsWebsite')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ReutersAd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
                ('news_website', models.ForeignKey(to='mysites.ReutersWebsite')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='aljazeeranews',
            name='checker_runtime',
        ),
        migrations.RemoveField(
            model_name='aljazeeranews',
            name='news_website',
        ),
        migrations.RemoveField(
            model_name='bbcnews',
            name='checker_runtime',
        ),
        migrations.RemoveField(
            model_name='bbcnews',
            name='news_website',
        ),
        migrations.RemoveField(
            model_name='reutersnews',
            name='checker_runtime',
        ),
        migrations.RemoveField(
            model_name='reutersnews',
            name='news_website',
        ),
        migrations.DeleteModel(
            name='AljazeeraNews',
        ),
        migrations.DeleteModel(
            name='BBCNews',
        ),
        migrations.DeleteModel(
            name='ReutersNews',
        ),
    ]
