from django.db import models

# Create your models here.
class MaximumAllowableStress(models.Model):
    spec_num = models.CharField(max_length=255)
    nominal_composition = models.CharField(max_length=50,default='Carbon Steel')
    product_form = models.CharField(max_length=255)
    type_grade = models.CharField(max_length=50)
    uns_num = models.CharField(max_length=50,)
    class_temper = models.CharField(max_length=50)
    size_thickness = models.CharField(max_length=50)
    p_num = models.CharField(max_length=50, default='1')
    group_num = models.CharField(max_length=50, default='1')
    min_tensile_strength = models.FloatField(default=0.0)
    min_yield_strength = models.FloatField(default=0.0)
    max_temp_I = models.CharField(max_length=50)
    max_temp_III = models.CharField(max_length=50)
    max_temp_VIII = models.CharField(max_length=50)
    max_temp_XII = models.CharField(max_length=50)
    ext_pressure_num = models.CharField(max_length=50)
    notes = models.CharField(max_length=255)
    max_stress_20_100 = models.FloatField(default=0.0)
    max_stress_150 = models.FloatField(default=0.0)
    max_stress_200 = models.FloatField(default=0.0)
    max_stress_250 = models.FloatField(default=0.0)
    max_stress_300 = models.FloatField(default=0.0)
    max_stress_400 = models.FloatField(default=0.0)
    max_stress_500 = models.FloatField(default=0.0)
    max_stress_600 = models.FloatField(default=0.0)
    max_stress_650 = models.FloatField(default=0.0)
    max_stress_700 = models.FloatField(default=0.0)
    max_stress_750 = models.FloatField(default=0.0)
    max_stress_800 = models.FloatField(default=0.0)
    max_stress_850 = models.FloatField(default=0.0)
    max_stress_900 = models.FloatField(default=0.0)
    max_stress_950 = models.FloatField(default=0.0)
    max_stress_1000 = models.FloatField(default=0.0)

    def __str__(self):
        return self.spec_num


class PipingSchedule(models.Model):
    pipe_size = models.FloatField(default=0.000)
    od_inch = models.FloatField(default=0.000)
    id_inch = models.FloatField(default=0.000)
    schedules = models.CharField(max_length=255)
    wall_inch = models.FloatField(default=0.000)
    est_wt = models.FloatField(default=0.0000)

    def __str__(self):
        return self.schedules