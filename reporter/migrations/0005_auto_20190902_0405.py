# Generated by Django 2.1.2 on 2019-09-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0004_merge_20190902_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='report',
            name='location_state',
            field=models.CharField(max_length=255),
        ),
    ]
