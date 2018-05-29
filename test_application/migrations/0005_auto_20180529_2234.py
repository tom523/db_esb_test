# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_application', '0004_newversionlog_oper_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newversionlog',
            name='create_time',
            field=models.DateTimeField(),
        ),
    ]
