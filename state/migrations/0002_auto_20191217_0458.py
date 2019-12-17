# Generated by Django 2.1.2 on 2019-12-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cylinderstate',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='headstate',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='nozzlestate',
            name='weight',
            field=models.FloatField(default=0.0),
        ),
    ]
