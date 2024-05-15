from rest_framework import serializers
from authApp.models.discount import Discount

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = [
            'discount_id',
            'date',
            'amount',
            'status'
        ]
    read_only_fields = [
        'discount_id',
        'date'
        ]

    def validate(self, data):
            if data.get('amount') <= 0:
                raise serializers.ValidationError("The amount, value must be positive.")
            if data.get('amount') > 100:
                raise serializers.ValidationError("The amount value must not exceed 100%.")
            return data