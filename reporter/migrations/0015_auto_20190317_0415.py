# Generated by Django 2.1.3 on 2019-03-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0014_auto_20190310_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='location',
            field=models.FilePathField(allow_folders=True, max_length=255, path='/home/grunz/Desktop/workspace/Pressure_Vessel/pressure_old/static/reports/'),
        ),
    ]