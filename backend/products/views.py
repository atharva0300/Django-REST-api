from django.shortcuts import render

# importing a generic view 
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

# importing the Response 
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

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

# post method tries to create something 
# the get method tries to list something


# creating an alt view to handle both the create and list/detail view which
# we have created above
@api_view(["GET", "POST"])
def product_alt_view(request , pk = None , *args , **kwargs) : 
    method = request.method

    if method == 'GET' :    
        # get request -> detail view 
        # list view

        if pk is not None : 
            # then details  view

            # get the object itself 
            obj = get_object_or_404(Product , pk = pk)
            # gives the object if it exists 
            # else 404 error 

            data = ProductSerializer(obj , many = False).data

            return Response(data) 
        
        else : 
            # a list view
            pass

        # create the list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset , many = True ).data
        # serializing the data

        return Response(data)

    elif method=='POST' : 
        
        # if post 
        # create an item 

        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True) : 
            # instance = serialize.save() 
            # instance = form.save()


            print(serializer.validated_data)
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')

            if content is None : 
                content = title

            serializer.save(content = content )

            # sending a django signal 


            print(serializer.data)
            return Response(serializer.data)
        
        return Response({"invalid" : "not good data"} , status = 400)
    



class ProductUpdateView(generics.UpdateAPIView) : 

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    # lookup for pk ? 
    lookup_field = 'pk'

    # performing an update 
    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content : 
            instance.content = instance.title
            ## not saving it initially 

        


product_update_view = ProductUpdateView.as_view()


class ProductDestroyView(generics.DestroyAPIView) : 

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    # lookup for pk ? 
    lookup_field = 'pk'

    # performing an update 
    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

        


product_destroy_view = ProductDestroyView.as_view()


