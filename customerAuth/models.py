from django.db import models
from django import forms
import uuid

# Create your models here.
class Customer(models.Model):
    customer_id = models.CharField(max_length=30,unique=True,default=str(uuid.uuid4()))
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10,default="1234567")

    def save(self,*args,**kwargs):
        if not self.customer_id:
            self.customer_id = str(uuid.uuid4())
        
        super().save(*args,**kwargs)

