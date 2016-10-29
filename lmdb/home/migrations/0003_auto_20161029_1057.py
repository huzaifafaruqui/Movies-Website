# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 10:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161027_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='actor',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='actor',
            name='last_name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='director',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='director',
            name='last_name',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='pictures/movie2.jpg', upload_to='static/images/products'),
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.Movie'),
        ),
    ]
