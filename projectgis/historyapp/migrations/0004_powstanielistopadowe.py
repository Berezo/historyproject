# Generated by Django 3.1 on 2021-01-23 10:14

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historyapp', '0003_powstaniestyczniowe'),
    ]

    operations = [
        migrations.CreateModel(
            name='PowstanieListopadowe',
            fields=[
                ('ogc_fid', models.AutoField(primary_key=True, serialize=False)),
                ('nazwa', models.CharField(blank=True, max_length=80, null=True)),
                ('typ', models.CharField(blank=True, max_length=80, null=True)),
                ('data', models.DateField(blank=True, null=True)),
                ('opis', models.CharField(blank=True, max_length=254, null=True)),
                ('str_kon_1', models.CharField(blank=True, max_length=80, null=True)),
                ('str_kon_2', models.CharField(blank=True, max_length=80, null=True)),
                ('dowod_1', models.CharField(blank=True, max_length=80, null=True)),
                ('dowod_2', models.CharField(blank=True, max_length=80, null=True)),
                ('zwyciestwo', models.CharField(blank=True, max_length=80, null=True)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=3857)),
            ],
            options={
                'db_table': 'powstanie_styczniowe',
                'ordering': ['data'],
                'managed': False,
            },
        ),
    ]
