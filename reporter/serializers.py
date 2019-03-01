# django rest framework
from rest_framework import serializers

# models form reporter app
from .models import Report, CylinderState, NozzleState

class ReportSerializer(serializers.ModelSerializer):
    # get user automatically from request
    # author = serializers.ReadOnlyField(source='author.username')
    # location = serializers.FilePathField()
    location = serializers.ReadOnlyField()
    # def create(self, validated_data):
    #     rep = Report(**validated_data)
    #     return rep.save()
    #     return Report.objects.create(**validated_data)
    class Meta:
        model = Report
        fields = ('id', 'created_at', 'report_type','location', 'author')

class CylinderStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CylinderState
        fields = '__all__'

class NozzleStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NozzleState
        fields = '__all__'