from rest_framework import serializers
from .models import Parameter

class ParameterSerializer(serializers.Serializer):
    spec_num = serializers.CharField(
        max_length= 255,
    )
    type_grade = serializers.CharField(
        max_length = 50,
    )
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
        model = Parameter
        fields = ['spec_num','type_grade','temp1','ip','sd','ic']