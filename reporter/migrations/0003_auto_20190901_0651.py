# Generated by Django 2.1.2 on 2019-09-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_auto_20190819_0550'),
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