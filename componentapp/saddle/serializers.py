from rest_framework import serializers
from asme.models import MaximumAllowableStress

class ParameterSerializer(serializers.ModelSerializer):

    vessel_spec_num = serializers.CharField(
        required=True,
        max_length=100,
    )
    vessel_type_grade = serializers.CharField(
        required=True,
        max_length=100,
    )
    vessel_diameter = serializers.FloatField(
        required=True,
    )
    vessel_thickness = serializers.FloatField(
        required=True,
    )
    vessel_corrosion_allowance = serializers.FloatField(
        required=True,
    )
    vessel_former_head_type = serializers.CharField(
        required=True,
        max_length=255,
    )
    vessel_head_height = serializers.FloatField(
        required=True,
    )
    vessel_design_pressure = serializers.FloatField(
        required=True,
    )
    vessel_design_temperature = serializers.IntegerField(
        required=True,
    )
    weld_joint_effiency = serializers.FloatField(
        default=1.0,
    )
    length_of_vessel = serializers.FloatField(
        required=True,
    )
    saddle_spec_num = serializers.CharField(
        required=True,
    )
    saddle_type_grade = serializers.CharField(
        required=True,
    )
    saddle_center_line_to_head = serializers.FloatField(
        required=True,
    )
    saddle_contact_angle = serializers.FloatField(
        required=True,
    )
    saddle_width = serializers.FloatField(
        required=True,
    )
    total_vessel_weight = serializers.FloatField(
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
        fields = ['vessel_spec_num',
                  'vessel_type_grade',
                  'vessel_diameter',
                  'vessel_thickness',
                  'vessel_corrosion_allowance',
                  'vessel_former_head_type',
                  'vessel_head_height',
                  'vessel_design_pressure',
                  'vessel_design_temperature',
                  'weld_joint_effiency',
                  'length_of_vessel',
                  'saddle_spec_num',
                  'saddle_type_grade',
                  'saddle_center_line_to_head',
                  'saddle_contact_angle',
                  'saddle_width',
                  'total_vessel_weight',
                  'projectID',
                  'componentID']