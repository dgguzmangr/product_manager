from rest_framework import serializers
from authApp.models.tax import Tax

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = [
            'tax_id',
            'name',
            'percentage',
            'status'
        ]
    read_only_fields = [
        'tax_id',
    ]

    def validate(self, data):
            if len(data.get('name', '')) > 100:
                raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
            if data.get('percentage') > 100:
                raise serializers.ValidationError("The amount value must not exceed 100%.")
            return data