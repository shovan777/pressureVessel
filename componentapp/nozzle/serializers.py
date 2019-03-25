from rest_framework import serializers
from asme.models import NozzleData,PipingSchedule

class NozzleSerializer(serializers.ModelSerializer):

    type_name =  serializers.CharField(
        max_length=10,
        required = True
    )
    nominal_pipe_size = serializers.FloatField(
        required = True,
    )
    class_value = serializers.IntegerField(
        max_value = 2500,
        min_value = 150,
        required = True,
    )
    spec_num = serializers.CharField(
        required = True,
    )
    type_grade = serializers.CharField(
        required = True,
    )
    temp1 = serializers.IntegerField(
        required = True,
    )
    designPressure = serializers.FloatField(
        required = True,
    )
    cylinderDiameter = serializers.FloatField(
        required = True,
    )
    corrosionAllowance = serializers.FloatField(
        required = True,
    )
    cylinderThickness = serializers.FloatField(
        required = True,
    )
    nozzleDiameter = serializers.FloatField(
        required = True,
    )
    externalNozzleProjection = serializers.FloatField(
        required = True,
    )
    internalNozzleProjection = serializers.FloatField(
        required = True,
    )
    projectID = serializers.IntegerField(
        required = True,
    )
    componentID = serializers.IntegerField(
        required = True,
    )
    class Meta:
        model = NozzleData
        # fields = ['nominal_pipe_size','type_name','class_value','projectID']
        fields = ['type_name','nominal_pipe_size','class_value','spec_num','type_grade','temp1','designPressure','cylinderDiameter','corrosionAllowance','cylinderThickness','nozzleDiameter','externalNozzleProjection','internalNozzleProjection','projectID','componentID']
