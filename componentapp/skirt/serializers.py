from rest_framework import serializers
from asme.models import MaximumAllowableStress

class ParameterSerializer(serializers.ModelSerializer):
    temp1 = serializers.IntegerField(
        required = True,
    )
    sd = serializers.FloatField(
        required = True,
    )
    ic = serializers.FloatField(
        required = True,
    )
    thickness = serializers.FloatField(
        required = True,
    )
    projectID = serializers.IntegerField(
        required = True,
    )
    length = serializers.FloatField(
        required = True,
    )

    class Meta:
        model = MaximumAllowableStress
        fields = ['spec_num','type_grade','temp1','sd','ic','thickness','length','projectID']