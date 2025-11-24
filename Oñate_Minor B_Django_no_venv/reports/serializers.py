# serializers.py
from rest_framework import serializers
from .models import Report, locationReport

class LocationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = locationReport
        fields = ['id', 'report', 'location', 'geolocation']


class ReportSerializer(serializers.ModelSerializer):
    pet_name = serializers.CharField(source='pet.name', read_only=True)
    reporter_username = serializers.CharField(source='reporter.username', read_only=True)
    locations = LocationReportSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = [
            'id',
            'pet',
            'pet_name',
            'reporter',
            'reporter_username',
            'description',
            'status',
            'timestamp',
            'locations',
        ]
