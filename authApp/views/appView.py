from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from djmoney.money import Money

from authApp.models.product import Product
from authApp.models.footprint import Footprint
from authApp.models.price import Price
from authApp.models.discount import Discount
from authApp.models.tax import Tax
from authApp.serializers.productSerializer import ProductSerializer
from authApp.serializers.footprintSerializer import FootprintSerializer
from authApp.serializers.priceSerializer import PriceSerializer
from authApp.serializers.discountSerializer import DiscountSerializer
from authApp.serializers.taxSerializer import TaxSerializer
from rest_framework.authtoken.models import Token # comentar par deshabilitar seguridad
from django.contrib.auth.forms import AuthenticationForm # comentar par deshabilitar seguridad
from django.contrib.auth import login as auth_login # comentar par deshabilitar seguridad

# Product API

@api_view(['GET'])
def show_products(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def show_product_prices(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    prices = Price.objects.filter(product=product)
    serializer = PriceSerializer(prices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def show_product_footprint(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        footprint = Footprint.objects.get(product=product)
    except Footprint.DoesNotExist:
        return Response({"error": "Footprint not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = FootprintSerializer(footprint)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def show_product_discounts(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    discounts = Discount.objects.filter(product=product)
    serializer = DiscountSerializer(discounts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def show_product_taxes(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    taxes = Tax.objects.filter(product=product)
    serializer = TaxSerializer(taxes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Footprint API

@api_view(['GET'])
def show_footprints(request):
    if request.method == 'GET':
        footprint = Footprint.objects.all()
        serializer = FootprintSerializer(footprint, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_footprint(request):
    if request.method == 'POST':
        serializer = FootprintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_footprint(request, pk):
    try:
        footprint = Footprint.objects.get(pk=pk)
    except Footprint.DoesNotExist:
        return Response({"error": "Footprint not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = FootprintSerializer(footprint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_footprint(request, pk):
    try:
        footprint = Footprint.objects.get(pk=pk)
    except Footprint.DoesNotExist:
        return Response({"error": "Footprint not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        footprint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Price API

@api_view(['GET'])
def show_prices(request):
    if request.method == 'GET':
        price = Price.objects.all()
        serializer = PriceSerializer(price, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_price(request):
    if request.method == 'POST':
        data = request.data
        amount = Money(data.get('amount'), data.get('currency'))
        price_data = {
            'amount': amount,
            'status': data.get('status')
            }
        serializer = PriceSerializer(data=price_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_price(request, pk):
    try:
        price = Price.objects.get(pk=pk)
    except Price.DoesNotExist:
        return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = PriceSerializer(price, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_price(request, pk):
    try:
        price = Price.objects.get(pk=pk)
    except Price.DoesNotExist:
        return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        price.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Discount API

@api_view(['GET'])
def show_discounts(request):
    if request.method == 'GET':
        discount = Discount.objects.all()
        serializer = DiscountSerializer(discount, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_discount(request):
    if request.method == 'POST':
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_discount(request, pk):
    try:
        discount = Discount.objects.get(pk=pk)
    except Discount.DoesNotExist:
        return Response({"error": "Discount not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DiscountSerializer(discount, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_discount(request, pk):
    try:
        discount = Discount.objects.get(pk=pk)
    except Discount.DoesNotExist:
        return Response({"error": "Discount not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        discount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Tax API

@api_view(['GET'])
def show_taxes(request):
    if request.method == 'GET':
        tax = Tax.objects.all()
        serializer = TaxSerializer(tax, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_tax(request):
    if request.method == 'POST':
        serializer = TaxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_tax(request, pk):
    try:
        tax = Tax.objects.get(pk=pk)
    except Tax.DoesNotExist:
        return Response({"error": "Tax not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TaxSerializer(tax, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_tax(request, pk):
    try:
        tax = Tax.objects.get(pk=pk)
    except Tax.DoesNotExist:
        return Response({"error": "Tax not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        tax.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)