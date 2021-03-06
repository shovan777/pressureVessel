# Generated by Django 2.1.3 on 2019-02-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asme', '0003_auto_20190205_1027'),
    ]

    operations = [
        migrations.CreateModel(
            name='NozzleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_value', models.IntegerField(default=150)),
                ('type_name', models.CharField(max_length=10)),
                ('nominal_pipe_size', models.FloatField(default=0.0)),
                ('flange_outer_diameter', models.FloatField(default=0.0)),
                ('flange_thickness', models.FloatField(default=0.0)),
                ('raised_face_diameter', models.FloatField(default=0.0)),
                ('blot_hole_number', models.IntegerField(default=0)),
                ('blot_hole_size', models.FloatField(default=0.0)),
                ('blot_circle_diameter', models.FloatField(default=0.0)),
                ('bore', models.FloatField(default=0.0)),
                ('barrel_outer_diameter', models.FloatField(default=0.0)),
            ],
        ),
        migrations.RenameField(
            model_name='pipingschedule',
            old_name='pipe_size',
            new_name='nominal_pipe_size',
        ),
        migrations.RenameField(
            model_name='pipingschedule',
            old_name='id_inch',
            new_name='pipe_internal_diameter_inch',
        ),
        migrations.RenameField(
            model_name='pipingschedule',
            old_name='od_inch',
            new_name='pipe_outer_diameter_inch',
        ),
    ]
