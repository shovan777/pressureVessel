from rest_framework import serializers
from asme.models import NozzleData,PipingSchedule

class NozzleSerializer(serializers.ModelSerializer):

    schedules = serializers.CharField(
        max_length = 20,
        required = True,
    )

    class_value = serializers.IntegerField(
        max_value = 2500,
        min_value = 150,
        required = True,
    )

    type_name =  serializers.CharField(
        max_length=10,
        required = True
    )

    nominal_pipe_size = serializers.FloatField(
        required = True,
    )

    # projectID = serializers.IntegerField(
    #     default = 1,
    # )

    class Meta:
        model = NozzleData
        # fields = ['nominal_pipe_size','type_name','class_value','schedules','projectID']
        fields = ['nominal_pipe_size','type_name','class_value','schedules']