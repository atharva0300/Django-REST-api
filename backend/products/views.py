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


class ProductCreateAPIView(generics.CreateAPIView) : 
    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    # getting the Product Serializer 

    def perform_create(self ,serializer) :
        serializer.save()
        # saving the serializer instance 

        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        # obtaining the title form the validated data
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        # checking if the content is there or not ? 
        if content is None : 
            content = title
        

        serializer.save(content = content) 

        # send a signal here ( a Django here )



product_create_api_view = ProductCreateAPIView.as_view()