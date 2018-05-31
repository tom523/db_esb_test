# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_application', '0005_auto_20180529_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newversionlog',
            name='storeid',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
