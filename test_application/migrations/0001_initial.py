# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewVersionFail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storeid', models.IntegerField()),
                ('storename', models.CharField(max_length=100)),
                ('create_time', models.DateField()),
                ('menu_version', models.ForeignKey(to='home_application.MenuVersion')),
            ],
        ),
        migrations.CreateModel(
            name='NewVersionSuccess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('storeid', models.IntegerField()),
                ('storename', models.CharField(max_length=100)),
                ('create_time', models.DateField()),
                ('menu_version', models.ForeignKey(to='home_application.MenuVersion')),
            ],
        ),
    ]
