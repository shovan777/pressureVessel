from rest_framework import serializers
from asme.models import PipingSchedule

class NozzleSerializer(serializers.ModelSerializer):

    ic = serializers.CharField(
        max_length = 50,
    )

    class Meta:
        model = PipingSchedule
        fields = ['schedules','ic']