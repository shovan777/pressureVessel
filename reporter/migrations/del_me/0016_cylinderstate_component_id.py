# Generated by Django 2.1.3 on 2019-03-17 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0015_auto_20190317_0415'),
    ]

    operations = [
        migrations.AddField(
            model_name='cylinderstate',
            name='component_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
