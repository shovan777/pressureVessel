from django.db import models

from reporter.models import Report

# Create your models here.
class Component(models.Model):
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        verbose_name = 'the related report'
        )
    react_component_id = models.IntegerField()
    type = models.CharField(max_length=100)
    def __str__(self):
        return str(self.react_component_id)
