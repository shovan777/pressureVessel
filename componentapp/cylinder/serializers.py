from rest_framework import serializers
from asme.models import MaximumAllowableStress

class ParameterSerializer(serializers.ModelSerializer):
    temp1 = serializers.FloatField(
        required = True,
    )
    ip = serializers.FloatField(
        required = True,
    )
    sd = serializers.FloatField(
        required = True,
    )
    ic = serializers.FloatField(
        required = True,
    )

    class Meta:
        model = MaximumAllowableStress
        fields = ['spec_num','type_grade','temp1','ip','sd','ic']