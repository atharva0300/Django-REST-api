from django.shortcuts import render

# importing a generic view 
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# importing app_view 
from rest_framework.decorators import api_view

# Create your views here.
class ProductDetailApiView(generics.RetrieveAPIView) : 
    # inheriting the retrive view 
    queryset = Product.objects.all()
    

    # serializing the data in the queryset 
    serializer_class = ProductSerializer
    # creating an instance of the ProductSerializer 
    # lookup field = 'pk'

    # Product.objects.get(pk = 'abc')

    def perform_create(self , serializer ) :
        # serializer.save(user = self.request.save)

        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None : 
            content = title

        serializer.save(content = content )

        # sending a django signal 

    
class ProductDetailListApiView(generics.ListAPIView) : 
    """
    
    Not gonna use this method
    
    because we can inherit ListCreateApiView in the above class 
    
    """
    queryset = Product.objects.all()

    serializer_class = ProductSerializer


product_detail_list_api_view = ProductDetailListApiView.as_view()



# converting the class to a view
product_detail_view = ProductDetailApiView.as_view()



class ProductCreateApiView(generics.CreateAPIView) : 
    queryset = Product.objects.all() 

    serializer_class = ProductSerializer



# naming convertion
product_create_api_view = ProductCreateApiView.as_view()