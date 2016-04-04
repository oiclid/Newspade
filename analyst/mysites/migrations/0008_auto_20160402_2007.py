# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '0017_added_order_to_scraped_obj_attr'),
        ('mysites', '0007_auto_20160402_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='AljazeeraNews',
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
            name='BBCNews',
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
            name='ReutersNews',
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
            model_name='aljazeeraad',
            name='checker_runtime',
        ),
        migrations.RemoveField(
            model_name='aljazeeraad',
            name='news_website',
        ),
        migrations.RemoveField(
            model_name='newsad',
            name='checker_runtime',
        ),
        migrations.RemoveField(
            model_name='newsad',
            name='news_website',
        ),
        migrations.RemoveField(
            model_name='reutersad',
            name='checker_runtime',
        ),
        migrations.RemoveField(
            model_name='reutersad',
            name='news_website',
        ),
        migrations.DeleteModel(
            name='AljazeeraAd',
        ),
        migrations.DeleteModel(
            name='NewsAd',
        ),
        migrations.DeleteModel(
            name='ReutersAd',
        ),
    ]
