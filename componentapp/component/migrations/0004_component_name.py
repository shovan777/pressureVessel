# Generated by Django 2.1.2 on 2019-04-28 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0003_remove_component_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='name',
            field=models.CharField(default='blank', max_length=100),
            preserve_default=False,
        ),
    ]