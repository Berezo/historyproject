# Generated by Django 3.1 on 2021-01-23 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('historyapp', '0007_auto_20210123_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='powstanielistopadowe',
            options={'ordering': ['data']},
        ),
        migrations.AlterModelOptions(
            name='powstaniestyczniowe',
            options={'ordering': ['data']},
        ),
        migrations.AlterModelOptions(
            name='rewolucjaamerykanska',
            options={'ordering': ['data']},
        ),
    ]