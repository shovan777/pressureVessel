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
        return self.report.__str__()


class NozzleState(models.Model):
    pass


class CentreOfGravity(models.Model):
    pass