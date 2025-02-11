from django.db import models
from django import forms

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name
