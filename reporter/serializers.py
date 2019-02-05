from rest_framework import serializers
from .models import Report, CylinderState, NozzleState

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class CylinderStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CylinderState
        fields = '__all__'

class NozzleStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NozzleState
        fields = '__all__'