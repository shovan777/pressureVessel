from rest_framework import serializers
from asme.models import MaximumAllowableStress

class HeadSerializer(serializers.ModelSerializer):
    temp1 = serializers.IntegerField(
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
    hr = serializers.CharField(
        required = True,
    )
    position = serializers.IntegerField(
        required = True,
    )
    projectID = serializers.IntegerField(
        required = True,
    )
    componentID = serializers.IntegerField(
        required = True,
    )

    class Meta:
        model = MaximumAllowableStress
        fields = ['spec_num','type_grade','temp1','ip','sd','ic','hr','position','projectID','componentID']