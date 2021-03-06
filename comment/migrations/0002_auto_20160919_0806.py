# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-09-19 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article', verbose_name='文章'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.IntegerField(choices=[('ok', '开启'), ('no', '关闭')], verbose_name='状态'),
        ),
    ]
