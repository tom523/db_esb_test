# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_application', '0003_auto_20180529_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='newversionlog',
            name='oper_user',
            field=models.CharField(default=b'admin', max_length=100),
        ),
    ]
