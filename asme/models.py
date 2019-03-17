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
    density = models.FloatField(default=0.0)
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
        return self.spec_num + "_" + self.type_grade


class PipingSchedule(models.Model):
    nominal_pipe_size = models.FloatField(default=0.000)
    pipe_outer_diameter_inch = models.FloatField(default=0.000)
    pipe_internal_diameter_inch = models.FloatField(default=0.000)
    schedules = models.CharField(max_length=255)
    wall_inch = models.FloatField(default=0.000)
    est_wt_pipe = models.FloatField(default=0.0000)

    def __str__(self):
        return str(self.nominal_pipe_size) + "_" + self.schedules

class NozzleData(models.Model):
    class_value = models.IntegerField(default=150)
    type_name =  models.CharField(max_length=10)
    nominal_pipe_size = models.FloatField(default=0.00)

    flange_outer_diameter = models.FloatField(default=0.00)
    flange_thickness = models.FloatField(default=0.00)
    raised_face_diameter = models.FloatField(default=0.00)
    blot_hole_number = models.IntegerField(default=0)
    blot_hole_size = models.FloatField(default=0.00)
    blot_circle_diameter = models.FloatField(default=0.00)
    bore = models.FloatField(default=0.00)
    barrel_outer_diameter = models.FloatField(default=0.00)
    
    nut_stop_diameter = models.FloatField(default=0.00)
    nut_relief_diameter = models.FloatField(default=0.00)
    nut_relief_length = models.FloatField(default=0.00)
    neck_thickness = models.FloatField(default=0.00)
    base_weight = models.FloatField(default=0.00)
    weight_per_one_inch = models.FloatField(default=0.00)
    base_weight_length = models.FloatField(default=0.00)
    raised_face_thickness = models.FloatField(default=0.00)

    def __str__(self):
        return self.type_name + "_" +str(self.class_value)+ "_" + str(self.nominal_pipe_size)
