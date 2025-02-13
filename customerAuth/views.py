from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
import uuid
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


@swagger_auto_schema(
    methods = ['post'],
    operation_description = "Endpoint to add a customer",
    request_body = CustomerSerializer
)
@api_view(['POST'])
def customer_add(request):
    request_payload = request.data
    serializer = CustomerSerializer(data=request_payload)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"msg":"invalid data format"},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def customer_delete(request,cust_id):
    try:
        data_to_be_deleted = Customer.objects.filter(customer_id = cust_id)
        data_to_be_deleted.delete()
        return Response({"msg":"Customer data deleted successfully"},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"msg":"Could not delete the desired customer data","error":str(e)},status = status.HTTP_500_INTERNAL_SERVER_ERROR)