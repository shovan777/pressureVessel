# django rest framework
from rest_framework import serializers

# models form reporter app
from .models import Report, CylinderState, NozzleState

class ReportSerializer(serializers.ModelSerializer):
    # get user automatically from request
    # author = serializers.ReadOnlyField(source='author.username')
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