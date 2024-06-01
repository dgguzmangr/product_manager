from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from djmoney.money import Money
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

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

@swagger_auto_schema(method='get', responses={200: ProductSerializer(many=True)} , tags=['Product'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def show_products(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=ProductSerializer, responses={201: ProductSerializer}, tags=['Product'])
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def create_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=ProductSerializer, responses={200: ProductSerializer}, tags=['Product'])
@api_view(['PUT'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
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

@swagger_auto_schema(method='patch', request_body=ProductSerializer, responses={200: ProductSerializer}, tags=['Product'])
@api_view(['PATCH'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def partial_update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Product'])
@api_view(['DELETE'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='get', responses={200: PriceSerializer(many=True)}, tags=['Product'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def show_product_prices(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    prices = Price.objects.filter(product=product)
    serializer = PriceSerializer(prices, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='get', responses={200: FootprintSerializer}, tags=['Product'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
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

@swagger_auto_schema(method='get', responses={200: DiscountSerializer(many=True)}, tags=['Product'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def show_product_discounts(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    discounts = Discount.objects.filter(product=product)
    serializer = DiscountSerializer(discounts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='get', responses={200: TaxSerializer(many=True)}, tags=['Product'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def show_product_taxes(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    taxes = Tax.objects.filter(product=product)
    serializer = TaxSerializer(taxes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Footprint API

@swagger_auto_schema(method='get', responses={200: FootprintSerializer(many=True)}, tags=['Footprint'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def show_footprints(request):
    if request.method == 'GET':
        footprint = Footprint.objects.all()
        serializer = FootprintSerializer(footprint, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=FootprintSerializer, responses={201: FootprintSerializer}, tags=['Footprint'])
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def create_footprint(request):
    if request.method == 'POST':
        serializer = FootprintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=FootprintSerializer, responses={200: FootprintSerializer}, tags=['Footprint'])
@api_view(['PUT'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
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

@swagger_auto_schema(method='patch', request_body=FootprintSerializer, responses={200: FootprintSerializer}, tags=['Footprint'])
@api_view(['PATCH'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def partial_update_footprint(request, pk):
    try:
        footprint = Footprint.objects.get(pk=pk)
    except Footprint.DoesNotExist:
        return Response({"error": "Footprint not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = FootprintSerializer(footprint, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Footprint'])
@api_view(['DELETE'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def delete_footprint(request, pk):
    try:
        footprint = Footprint.objects.get(pk=pk)
    except Footprint.DoesNotExist:
        return Response({"error": "Footprint not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        footprint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Price API

@swagger_auto_schema(method='get', responses={200: PriceSerializer(many=True)}, tags=['Price'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def show_prices(request):
    if request.method == 'GET':
        price = Price.objects.all()
        serializer = PriceSerializer(price, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'amount': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
            'amount': openapi.Schema(type=openapi.TYPE_NUMBER, description='Amount value'),
            'currency': openapi.Schema(type=openapi.TYPE_STRING, description='Currency code')
        }),
        'status': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Status of the price')
    }
), responses={201: PriceSerializer}, tags=['Price'])
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def create_price(request):
    if request.method == 'POST':
        serializer = PriceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=PriceSerializer, responses={200: PriceSerializer}, tags=['Price'])
@api_view(['PUT'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
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

@swagger_auto_schema(method='patch', request_body=PriceSerializer, responses={200: PriceSerializer}, tags=['Price'])
@api_view(['PATCH'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def partial_update_price(request, pk):
    try:
        price = Price.objects.get(pk=pk)
    except Price.DoesNotExist:
        return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = PriceSerializer(price, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Price'])
@api_view(['DELETE'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def delete_price(request, pk):
    try:
        price = Price.objects.get(pk=pk)
    except Price.DoesNotExist:
        return Response({"error": "Price not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        price.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Discount API

@swagger_auto_schema(method='get', responses={200: DiscountSerializer(many=True)}, tags=['Discount'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def show_discounts(request):
    if request.method == 'GET':
        discount = Discount.objects.all()
        serializer = DiscountSerializer(discount, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=DiscountSerializer, responses={201: DiscountSerializer}, tags=['Discount'])
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def create_discount(request):
    if request.method == 'POST':
        serializer = DiscountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=DiscountSerializer, responses={200: DiscountSerializer}, tags=['Discount'])
@api_view(['PUT'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
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

@swagger_auto_schema(method='patch', request_body=DiscountSerializer, responses={200: DiscountSerializer}, tags=['Discount'])
@api_view(['PATCH'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def partial_update_discount(request, pk):
    try:
        discount = Discount.objects.get(pk=pk)
    except Discount.DoesNotExist:
        return Response({"error": "Discount not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = DiscountSerializer(discount, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Discount'])
@api_view(['DELETE'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def delete_discount(request, pk):
    try:
        discount = Discount.objects.get(pk=pk)
    except Discount.DoesNotExist:
        return Response({"error": "Discount not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        discount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Tax API

@swagger_auto_schema(method='get', responses={200: TaxSerializer(many=True)}, tags=['Tax'])
@api_view(['GET'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def show_taxes(request):
    if request.method == 'GET':
        tax = Tax.objects.all()
        serializer = TaxSerializer(tax, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(method='post', request_body=TaxSerializer, responses={201: TaxSerializer}, tags=['Tax'])
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def create_tax(request):
    if request.method == 'POST':
        serializer = TaxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='put', request_body=TaxSerializer, responses={200: TaxSerializer}, tags=['Tax'])
@api_view(['PUT'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
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

@swagger_auto_schema(method='patch', request_body=TaxSerializer, responses={200: TaxSerializer}, tags=['Tax'])
@api_view(['PATCH'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def partial_update_tax(request, pk):
    try:
        tax = Tax.objects.get(pk=pk)
    except Tax.DoesNotExist:
        return Response({"error": "Tax not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = TaxSerializer(tax, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='delete', responses={204: 'No Content'}, tags=['Tax'])
@api_view(['DELETE'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def delete_tax(request, pk):
    try:
        tax = Tax.objects.get(pk=pk)
    except Tax.DoesNotExist:
        return Response({"error": "Tax not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        tax.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Login API

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the user'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user')
        }
    ),
    responses={
        200: openapi.Response(
            description="Successful login",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token')
                }
            )
        ),
        400: openapi.Response(
            description="Invalid username or password",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message')
                }
            )
        )
    },
    tags=['Authentication']
)
@api_view(['POST'])
@permission_classes([])  # Comentar o modificar según sea necesario para producción
@authentication_classes([])  # Comentar o modificar según sea necesario para producción
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)