from rest_framework import serializers
from asme.models import MaximumAllowableStress

class ParameterSerializer(serializers.ModelSerializer):
    temp1 = serializers.FloatField(
        max_value = 250,
        min_value = 2,
        required = True,
    )
    ip = serializers.FloatField(
        max_value = 50,
        min_value = 2,
        required = True,
    )
    sd = serializers.FloatField(
        max_value = 50,
        min_value = 2,
        required = True,
    )
    ic = serializers.FloatField(
        max_value = 60,
        min_value = 2,
        required = True,
    )

    class Meta:
        model = MaximumAllowableStress
        fields = ['spec_num','type_grade','temp1','ip','sd','ic']