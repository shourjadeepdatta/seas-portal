from django.urls import path
from . import views

urlpatterns = [
    path("health",views.health,name="health"),
    path("list",views.customer_list,name="customer_list"),
    path("add",views.customer_add,name="customer_add")    
]