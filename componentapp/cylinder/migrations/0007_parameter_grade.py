# Generated by Django 2.1.2 on 2018-10-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cylinder', '0006_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='grade',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
    ]