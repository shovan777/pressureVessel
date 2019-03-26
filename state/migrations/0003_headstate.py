# Generated by Django 2.1.2 on 2019-03-26 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0003_remove_component_material'),
        ('reporter', '0020_auto_20190326_0728'),
        ('state', '0002_auto_20190325_0644'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('P', models.FloatField(default=0.0)),
                ('D_o', models.FloatField(default=0.0)),
                ('K', models.FloatField(default=0.0)),
                ('S', models.FloatField(default=0.0)),
                ('E', models.FloatField(default=0.0)),
                ('C_A', models.FloatField(default=0.0)),
                ('t', models.FloatField(default=0.0)),
                ('component', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='component.Component')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Report', verbose_name='the related report')),
            ],
        ),
    ]
