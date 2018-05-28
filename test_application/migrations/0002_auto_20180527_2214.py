# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '__first__'),
        ('test_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewVersionLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storeid', models.IntegerField(unique=True)),
                ('storename', models.CharField(max_length=100)),
                ('create_time', models.DateField()),
                ('success', models.BooleanField()),
                ('menu_version', models.ForeignKey(to='home_application.MenuVersion')),
            ],
        ),
        migrations.RemoveField(
            model_name='newversionfail',
            name='menu_version',
        ),
        migrations.RemoveField(
            model_name='newversionsuccess',
            name='menu_version',
        ),
        migrations.DeleteModel(
            name='NewVersionFail',
        ),
        migrations.DeleteModel(
            name='NewVersionSuccess',
        ),
    ]
