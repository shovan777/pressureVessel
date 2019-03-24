# django rest framework
from rest_framework import serializers

# models from reporter app
from reporter.models import Report

# models form component app
from .models import Component

class ComponentSerializer(serializers.ModelSerializer):
    # put some code here
    # somewhere you must get the reportid
    def _get_report(self, id):
        return Report.objects.get(pk=id)

    class Meta:
        model = Component
        fields = ('id', 'react_component_id', 'type')

    def create(self, validated_data):
        report_id = validated_data.pop('report_id')
        validated_data['report'] = self._get_report(report_id)
        return Component.objects.create(**validated_data)
