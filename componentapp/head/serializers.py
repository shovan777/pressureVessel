from rest_framework import serializers
from asme.models import MaximumAllowableStress

class HeadSerializer(serializers.ModelSerializer):
    temp1 = serializers.CharField(
        max_length = 50,
    )
    ip = serializers.CharField(
        max_length = 50,
    )
    sd = serializers.CharField(
        max_length = 50,
    )
    ic = serializers.CharField(
        max_length = 50,
    )

    class Meta:
        model = MaximumAllowableStress
        fields = ['spec_num','type_grade','temp1','ip','sd','ic']