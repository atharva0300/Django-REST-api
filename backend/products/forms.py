from django import forms 

# we import serializers from rest framework 
from rest_framework import serializers


from .models import Product

class ProductForm(serializers.ModelSerializer) : 
    # inherit the ModelSerializer
    # so that we can display the sale price ( which is a decorator function value and not an actual field )
    class Meta : 
        model = Product

        fields = ['title' , 'content' , 'price' , 'sale_price' , 'get_discount']