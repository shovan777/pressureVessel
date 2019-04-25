# django imports
from django.db import models

# component app models
from componentapp.component.models import Component

# reporter app models
from reporter.models import Report

class CylinderState(models.Model):
    # cylinder state has a many to one relationship with report
    # becaUSE a report may have multiple cylinders
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        verbose_name='the related report'
    )
    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE
    )
    D = models.FloatField(default=0.0)
    C_A = models.FloatField(default=0.0)
    P = models.FloatField(default=0.0)
    R = models.FloatField(default=0.0)
    S = models.FloatField(default=0.0)
    E = models.FloatField(default=0.0)
    t_inter = models.FloatField(default=0.0)
    t = models.FloatField(default=0.0)

    def __str__(self):
        # return self.id or something like that
        return self.component.__str__()


class NozzleState(models.Model):
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        verbose_name='the related report'
    )
    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE
    )
    L_R = models.FloatField(default=0.0)
    d = models.FloatField(default=0.0)
    R_n = models.FloatField(default=0.0)
    C_n = models.FloatField(default=0.0)
    t_n = models.FloatField(default=0.0)
    t = models.FloatField(default=0.0)
    L_H = models.FloatField(default=0.0)
    t_e = models.FloatField(default=0.0)
    t_rn = models.FloatField(default=0.0)
    P = models.FloatField(default=0.0)
    S_n = models.FloatField(default=0.0)
    E = models.FloatField(default=0.0)
    t_r = models.FloatField(default=0.0)
    R_o = models.FloatField(default=0.0)
    msg = models.TextField()

    def __str__(self):
        # return self.id or something like that
        return self.component.__str__()

class HeadState(models.Model):
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        verbose_name='the related report'
    )
    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE
    )
    position = models.CharField(max_length=50)
    P = models.FloatField(default=0.0)
    D_o = models.FloatField(default=0.0)
    K = models.FloatField(default=0.0)
    S = models.FloatField(default=0.0)
    E = models.FloatField(default=0.0)
    C_A = models.FloatField(default=0.0)
    t = models.FloatField(default=0.0)

    def __str__(self):
        # return self.id or something like that
        return self.component.__str__()


class LiftingLugState(models.Model):
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        verbose_name='the related report'
    )
    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE
    )
    W = models.FloatField(default=0.0)
    phi = models.FloatField(default=0.0)
    x_1 = models.FloatField(default=0.0)
    x_2 = models.FloatField(default=0.0)
    F_r = models.FloatField(default=0.0)
    d_reqd = models.FloatField(default=0.0)
    diameter_ratio = models.FloatField(default=0.0)
    D_p = models.FloatField(default=0.0)
    sigma_sd_calc = models.FloatField(default=0.0)
    sigma_sd_ratio = models.FloatField(default=0.0)
    t_reqd_tensile = models.FloatField(default=0.0)
    L = models.FloatField(default=0.0)
    d = models.FloatField(default=0.0)
    sigma_t = models.FloatField(default=0.0)
    sigma_b = models.FloatField(default=0.0)
    sigma_t_calc = models.FloatField(default=0.0)
    sigma_t_ratio = models.FloatField(default=0.0)
    t = models.FloatField(default=0.0)
    t_reqd_bearing = models.FloatField(default=0.0)
    A_bearing = models.FloatField(default=0.0)
    sigma_b_calc = models.FloatField(default=0.0)
    sigma_b_ratio = models.FloatField(default=0.0)
    phi_shear = models.FloatField(default=0.0)
    L_shear = models.FloatField(default=0.0)
    H = models.FloatField(default=0.0)
    a_2 = models.FloatField(default=0.0)
    t_reqd_shear = models.FloatField(default=0.0)
    t_max = models.FloatField(default=0.0)
    thickness_ratio = models.FloatField(default=0.0)
    A_shear = models.FloatField(default=0.0)
    tau = models.FloatField(default=0.0)
    sigma_s = models.FloatField(default=0.0)
    sigma_s_ratio = models.FloatField(default=0.0)
    A_weld = models.FloatField(default=0.0)
    t_w = models.FloatField(default=0.0)
    alpha = models.FloatField(default=0.0)
    tau_t = models.FloatField(default=0.0)
    tau_s = models.FloatField(default=0.0)
    M = models.FloatField(default=0.0)
    Hght = models.FloatField(default=0.0)
    c = models.FloatField(default=0.0)
    h = models.FloatField(default=0.0)
    l = models.FloatField(default=0.0)
    tau_b = models.FloatField(default=0.0)
    tau_allowable = models.FloatField(default=0.0)
    tau_ratio = models.FloatField(default=0.0)
    lug_pin_check = models.BooleanField(default=False)
    lug_thickness_check = models.BooleanField(default=False)
    shear_thickness_check = models.BooleanField(default=False)
    shear_diameter_check = models.BooleanField(default=False)
    tensile_check = models.BooleanField(default=False)
    bearing_check = models.BooleanField(default=False)

    def __str__(self):
        # return self.id or something like that
        return self.component.__str__()


class SkirtState(models.Model):
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        verbose_name='the related report'
    )
    component = models.OneToOneField(
        Component,
        on_delete=models.CASCADE
    )
    response_skirt = models.CharField(max_length=255)
    thickness = models.FloatField(default=0.0)
    corrosion_allowance = models.FloatField(default=0.0)

    def __str__(self):
        return self.component.__str__()


class CentreOfGravity(models.Model):
    pass
