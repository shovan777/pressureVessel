# Generated by Django 2.1.2 on 2019-04-14 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reporter', '0022_auto_20190407_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='author_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ReportCreator'),
            preserve_default=False,
        ),
    ]