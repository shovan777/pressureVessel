# Generated by Django 2.1.2 on 2019-02-17 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0005_auto_20190210_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='author',
            field=models.CharField(default='shovan', max_length=100),
        ),
    ]
