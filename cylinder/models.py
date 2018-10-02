from django.db import models

# Create your models here.
class Parameter(models.Model):
    # thickness = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    strength = models.FloatField(default=1)
