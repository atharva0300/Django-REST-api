from django.shortcuts import render

# importing a generic view 
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductDetailApiView(generics.RetrieveAPIView) : 
    # inheriting the retrive view 
    queryset = Product.objects.all()
    

    # serializing the data in the queryset 
    serializer_class = ProductSerializer
    # creating an instance of the ProductSerializer 
    # lookup field = 'pk'

    # Product.objects.get(pk = 'abc')


# converting the class to a view
product_detail_view = ProductDetailApiView.as_view()