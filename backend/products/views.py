from django.shortcuts import render

# Create your views here.
from rest_framework import generics 

from .models import Product
from .serializers import ProductSerializer

# importing the api_view and the Response to convert the normal Django APi to the REST API 
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.shortcuts import get_object_or_404


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


class ProductListCreateAPIView(generics.ListCreateAPIView) : 
    # ListCreateAPI View is a combination of both create and list APi View 
    # Create API View is called when -> the request.method is 'POST' request -> you are trying to create a new Product
    # List API View is called when -> the request.method is a 'GET' request -> you are trying to get the list of all the Products


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



product_list_create_api_view = ProductListCreateAPIView.as_view()



class ProductListAPIView(generics.ListAPIView) : 
    """
    
    NOT Gonna use this method

    """
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



@api_view(['GET' , 'POST'])
def product_alt_view(request , pk = None,  *args , **kwargs) : 
    method = request.method

    if method=='GET' : 
        # get request -> detail view 
        if pk is not None : 
            # detail view
            obj =  get_object_or_404(Product , pk = pk)
            # getting the object with the pk 
            data = ProductSerializer(obj , many = False)    # one item only

            return Response()
        

        # list view
        # creating a queryset 
        queryset = Product.objects.all()

        data = ProductSerializer(queryset , many = True).data

        return Response(data)
    
    elif method=='POST' : 
        # create an item ( product )

        serializer = ProductSerializer(data =request.data)
        
        if serializer.is_valid(raise_exception=True) : 
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

            return Response(serializer.data)

        return Response({"invlid" : "Not a good data"} , status = 400)


