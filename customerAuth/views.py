from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
# Create your views here.

def health(request):
    return HttpResponse("Hello and api is fine")


@api_view(['GET', 'POST'])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        print(customers)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def customer_add(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"msg":"invalid data format"},status=status.HTTP_400_BAD_REQUEST)