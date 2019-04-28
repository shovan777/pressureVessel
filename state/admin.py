from django.contrib import admin
from .models import CylinderState,SkirtState,NozzleState,HeadState,LiftingLugState,CentreOfGravity

# Register your models here.
admin.site.register(CylinderState)
admin.site.register(SkirtState)
admin.site.register(NozzleState)
admin.site.register(HeadState)
admin.site.register(LiftingLugState)
admin.site.register(CentreOfGravity)