from django.shortcuts import render

# Create your views here.
from rest_framework import generics 

from .models import Product
from .serializers import ProductSerializer



# creating a ProductDetailAPIView
class ProductDetailAPIView(generics.RetrieveAPIView) : 
    
    # get the queryset 
    queryset = Product.objects.all()

    # creating a product serializer
    serializer_class = ProductSerializer

    # lookup_field = 'pk'
    # Product.objects.get(pk = 2)


product_detail_api_view = ProductDetailAPIView.as_view()
# this will convert the class api view as a Django understandable view 