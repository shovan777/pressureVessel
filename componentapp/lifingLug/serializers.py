"""Serialize data for lifting lug."""
from rest_framework import serializers
from asme.models import MaximumAllowableStress


class LiftingLugSerializer(serializers.ModelSerializer):
    length = serializers.FloatField(
        required=True,
    )
    height = serializers.FloatField(
        required=True,
    )
    hole_diameter = serializers.FloatField(
        required=True,
    )
    thickness = serializers.FloatField(
        required=True,
    )
    pin_diameter = serializers.FloatField(
        required=True,
    )
    load_eccentricity = serializers.FloatField(
        required=True,
    )
    distance_load_to_shell = serializers.FloatField(
        required=True,
    )
    normal_load_angle = serializers.FloatField(
        required=True,
    )
    vertical_load_angle = serializers.FloatField(
        required=True,
    )
    weld_size = serializers.FloatField(
        required=True,
    )
    lug1_cg_distance = serializers.FloatField(
        required=True,
    )
    lug2_cg_distance = serializers.FloatField(
        required=True,
    )
    projectID = serializers.IntegerField(
        required=True,
    )
    componentID = serializers.IntegerField(
        required=True,
    )

    class Meta:
        model = MaximumAllowableStress
        fields = ['spec_num', 'type_grade', 'length', 'height', 'thickness', 'hole_diameter', 'pin_diameter',
                  'load_eccentricity', 'distance_load_to_shell', 'normal_load_angle', 'vertical_load_angle',
                  'weld_size', 'lug1_cg_distance', 'lug2_cg_distance', 'projectID', 'componentID']
