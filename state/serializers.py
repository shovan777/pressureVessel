# django rest framework
from rest_framework import serializers

# models form reporter app
from .models import CylinderState, NozzleState


class CylinderStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CylinderState
        fields = '__all__'

class NozzleStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NozzleState
        fields = '__all__'