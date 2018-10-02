from django.db import models

# Create your models here.
class Parameter(models.Model):
    thickness = models.IntegerField(default=0)
