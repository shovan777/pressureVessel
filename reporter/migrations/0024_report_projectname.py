# Generated by Django 2.1.2 on 2019-04-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0023_report_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='projectName',
            field=models.CharField(default=22, max_length=100),
            preserve_default=False,
        ),
    ]
