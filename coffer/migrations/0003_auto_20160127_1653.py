# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffer', '0002_auto_20151012_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='description_markup_type',
            field=models.CharField(choices=[(b'', b'--'), (b'html', 'HTML'), (b'plain', 'Plain'), (b'markdown', 'Markdown')], default=b'markdown', editable=False, max_length=30),
        ),
    ]