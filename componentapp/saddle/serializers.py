from rest_framework import serializers
from asme.models import MaximumAllowableStress

class ParameterSerializer(serializers.ModelSerializer):
    projectID = serializers.IntegerField(
        required = True,
    )
    componentID = serializers.IntegerField(
        required = True,
    )

    class Meta:
        model = MaximumAllowableStress
        fields = ['projectID','componentID']
