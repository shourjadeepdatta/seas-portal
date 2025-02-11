from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'  # Includes all fields from the model
        extra_kwargs = {'password': {'write_only': True}}  # Hide password from responses
