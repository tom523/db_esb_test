# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_application', '0002_auto_20180527_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newversionlog',
            name='success',
        ),
        migrations.AddField(
            model_name='newversionlog',
            name='oper_type',
            field=models.CharField(default='\u53d1\u7248', max_length=100),
        ),
    ]
