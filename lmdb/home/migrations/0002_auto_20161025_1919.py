# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-25 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(default='pictures/movie2.jpg', upload_to='pic_folder/'),
        ),
    ]