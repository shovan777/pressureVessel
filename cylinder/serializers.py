from rest_framework import serializers
from cylinder.models import Parameter

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'