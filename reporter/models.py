from django.db import models
from userapp.models import User

def report_path(instance, location):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance, instance.id)
    return '{0}/{1}.pdf'.format(location, instance.id)

#  Create your models here.
class Report(models.Model):
    report_type = models.CharField(max_length=50)
    location = models.FileField(upload_to=report_path)
    author = models.CharField(max_length=100, default='shovan')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
    def __str__(self):
        return '%s' %(self.location)

class CylinderState(models.Model):
    # cylinder state has a many to one relationship with report
    # becaUSE a report may have multiple cylinders
    report = models.ForeignKey(
        Report, 
        on_delete=models.CASCADE,
        verbose_name = 'the related report'
        )
    D = models.FloatField(default=0.0)
    C_A = models.FloatField(default=0.0)
    P = models.FloatField(default=0.0)
    R = models.FloatField(default=0.0)
    S = models.FloatField(default=0.0)
    E = models.FloatField(default=0.0)
    t = models.FloatField(default=0.0)

    def __str__(self):
        # return self.id or something like that
        pass

class NozzleState(models.Model):
    pass