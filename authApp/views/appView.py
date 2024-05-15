from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from authApp.models.product import Product
from authApp.models.footprint import Footprint
from authApp.serializers.productSerializer import ProductSerializer
from authApp.serializers.footprintSerializer import FootprintSerializer

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