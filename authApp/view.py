"""
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class MyAPIView(APIView):
    def get(self, request):
        # Código para manejar las solicitudes GET
        return Response({'message': 'GET request processed'})

    def post(self, request):
        # Código para manejar las solicitudes POST
        return Response({'message': 'POST request processed'})
# Create your views here.
"""