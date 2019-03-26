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


class CentreOfGravity(models.Model):
    pass