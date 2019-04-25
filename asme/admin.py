from django.contrib import admin
from .models import MaximumAllowableStress,PipingSchedule,NozzleData

# Register your models here.
admin.site.register(MaximumAllowableStress)
admin.site.register(PipingSchedule)
admin.site.register(NozzleData)