# django imports
from django.db import models

# userapp models
from userapp.models import User



# from settings
from pressureVessel import settings

static_report_path = settings.STATIC_ROOT + 'reports/'


# this is a deprecated method
# del_me
def report_path(instance, filename='report'):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # print('\n\n********************')
    # print(instance, instance.author, instance.report_type, instance.created_at.time().strftime('%H-%M-%S'))
    return 'user_{0}/{1}/{2}/{3}.pdf'.format(instance.author, instance.created_at.date(), instance.created_at.time().strftime('%H-%M-%S'), 'report')

#  Create your models here.


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(max_length=50)
    location = models.FilePathField(
        path=static_report_path, allow_folders=True, max_length=255)
    author = models.CharField(max_length=100, default='shovan')
    author_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='ReportCreator'
    )

    def report_path(self, filename='report'):
        return 'user_{0}/{1}/{2}/{3}.pdf'.format(self.author, self.created_at.date(), self.created_at.time().strftime('%H-%M-%S'), filename)

    def save(self, filename, *args, **kwargs):
        flag = 0
        if not self.pk:
            flag = 1
        super(Report, self).save(*args, **kwargs)
        if flag:
            self.location = static_report_path + self.report_path(filename=filename)
            flag = 0
            self.save(filename=filename)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return '%s' % (self.location)



