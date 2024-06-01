from rest_framework import serializers
from authApp.models.price import Price
from djmoney.money import Money

class MoneyField(serializers.Field):
    def to_representation(self, value):
        return {
            'amount': value.amount,
            'currency': value.currency.code
        }

    def to_internal_value(self, data):
        try:
            amount = data['amount']
            currency = data['currency']
            return Money(amount, currency)
        except KeyError:
            raise serializers.ValidationError("Amount and currency are required fields.")
        except TypeError:
            raise serializers.ValidationError("Incorrect type. Expected a dictionary with 'amount' and 'currency'.")

class PriceSerializer(serializers.ModelSerializer):
    amount = MoneyField()

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
