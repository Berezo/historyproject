# Generated by Django 3.1 on 2021-01-23 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historyapp', '0005_auto_20210123_1117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wojnatrzydziestoletnia',
            options={'ordering': ['data']},
        ),
    ]
