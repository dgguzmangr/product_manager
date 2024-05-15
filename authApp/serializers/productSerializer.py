from rest_framework import serializers
from authApp.models.product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'product_id',
            'sku',
            'name',
            'short_description',
            'long_description',
            'footprint',
            'price',
            'discount',
            'tax'
            ]
        read_only_fields = [
            'product_id',
            'sku'
            ]

        def validate(self, data):
            if len(data.get('name', '')) > 100:
                raise serializers.ValidationError("The 'name' field cannot exceed 100 characters.")
            if len(data.get('short_description', '')) > 30:
                raise serializers.ValidationError("The 'short_description' field cannot exceed 30 characters.")
            if len(data.get('long_description', '')) > 100:
                raise serializers.ValidationError("The 'long_description' field cannot exceed 100 characters.")
            return data
