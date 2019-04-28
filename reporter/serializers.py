# django rest framework
from rest_framework import serializers

# models form reporter app
from .models import Report
class ReportSerializer(serializers.ModelSerializer):
    # get user automatically from request
    # author = serializers.ReadOnlyField(source='author.username')
    # location = serializers.FilePathField()
    location = serializers.ReadOnlyField()
    location_state = serializers.ReadOnlyField()
    # def create(self, validated_data):
    #     rep = Report(**validated_data)
    #     return rep.save()
    #     return Report.objects.create(**validated_data)
    class Meta:
        model = Report
        fields = ('id', 'created_at', 'report_type', 'location', 'location_state', 'author', 'projectName', 'orientation')
        
class ReportInputSerializer(serializers.ModelSerializer):

    report_type = serializers.CharField(
        required=True,
    )
    projectName = serializers.CharField(
        required=True,
    )
    orientation = serializers.CharField(
        required=True,
    )

    class Meta:
        model = Report
        fields = ['report_type', 'projectName', 'orientation']
