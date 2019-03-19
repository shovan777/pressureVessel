# rest framework modules
from rest_framework import viewsets

# state modules
from .models import CylinderState, NozzleState, Report
from reporter.serializers import CylinderStateSerializer, NozzleStateSerializer


class CylinderStateViewSet(viewsets.ModelViewSet):
    queryset = CylinderState.objects.all()
    serializer_class = CylinderStateSerializer


class NozzleStateViewSet(viewsets.ModelViewSet):
    queryset = NozzleState.objects.all()
    serializer_class = NozzleStateSerializer

