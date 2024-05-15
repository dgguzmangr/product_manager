from rest_framework import serializers
from authApp.models import Footprint

class FootprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footprint
        fields = [
            'footprint_id', 
            'measurement_unit', 
            'long', 
            'high', 
            'width', 
            'weight', 
            'volume'
            ]
        read_only_fields = ['footprint_id, volume']

        def validate(self, data):
            if data.get('long') <= 0 or data.get('high') <= 0 or data.get('width') <= 0:
                raise serializers.ValidationError("The long, high and width values must be positive.")
            return data
