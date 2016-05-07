# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 19:43
from __future__ import unicode_literals

from django.db import migrations, models

import pretix.base.i18n


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0019_auto_20160326_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcategory',
            name='description',
            field=pretix.base.i18n.I18nTextField(blank=True, verbose_name='Category description'),
        ),
        migrations.AlterField(
            model_name='questionanswer',
            name='options',
            field=models.ManyToManyField(blank=True, related_name='answers', to='pretixbase.QuestionOption'),
        ),
    ]