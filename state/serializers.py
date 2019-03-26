# django rest framework
from rest_framework import serializers

# models form reporter app
from .models import CylinderState, NozzleState, HeadState


class CylinderStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CylinderState
        fields = '__all__'

class NozzleStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NozzleState
        fields = '__all__'

class HeadStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HeadState
        fields = '__all__'

