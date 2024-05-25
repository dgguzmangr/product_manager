from rest_framework import serializers
from authApp.models.price import Price
from djmoney.money import Money

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

    def validate_amount(self, value):
        if value.amount <= 0:
            raise serializers.ValidationError("The amount must be positive.")
        return value




