# Generated by Django 3.1 on 2021-01-17 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wojnatrzydziestoletnia',
            options={'managed': False, 'ordering': ['data']},
        ),
    ]