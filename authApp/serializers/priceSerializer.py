from rest_framework import serializers
from authApp.models.price import Price

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = [
            'price_id',
            'amount',
            'date',
            'status'
        ]
    read_only_fields = [
        'price_id', 
        'date'
        ]

    def validate(self, data):
            if data.get('amount') <= 0:
                raise serializers.ValidationError("The amount, value must be positive.")
            return data




