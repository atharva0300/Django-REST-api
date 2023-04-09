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

# importing the mixins 
from rest_framework import mixins

# importing authentication and permissions from rest framework 
from rest_framework import permissions , authentication

# Create your views here.
class ProductDetailApiView(generics.RetrieveAPIView) : 
    # inheriting the retrive view 
    queryset = Product.objects.all()

    # creating permission classes 

    authentication_classes = [authentication.SessionAuthentication]
    # the authentication.SessionAuthentication will check authentication for the user for the session

    # a look into "Session Authentication and Permissions"
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # a builtin list to manage permissions
    # setting the permission as it Authenticated
    # permissions.IsAuthenticatedOrReadOnly and permission.IsAutenticated

    """
    If not authenticated, then the request api will not return anything but will return 
    {
    "detail": "Authentication credentials were not provided."
    }
    
    """
    
    

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

    def post(self , request , *args , **kwargs) :    # HTTP -> post 
        return self.list(request  , *args , **kwargs)
        # returning the list of the requet , args and kwargs 


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

# class to create an api view 
class CreateApiView(mixins.CreateModelMixin , generics.GenericAPIView) : 
    pass 


# this mixin is performing all the operations 
class ProductMixinView(mixins.CreateModelMixin , mixins.ListModelMixin , mixins.RetrieveModelMixin , generics.GenericAPIView): 

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # setting the lookup field as the pk


    def post(self , request , *args , **kwargs) :    # HTTP -> post 
        return self.create(request  , *args , **kwargs)
        # creating the list of the requet , args and kwargs 
        # an returning it


    def perform_create(self , serializer ) :
        # serializer.save(user = self.request.save)

        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None : 
            content = "This is a single view doing cool stuff"

        serializer.save(content = content )

        # sending a django signal 
    def get(self , request , *args , **kwargs) :    # HTTP -> get 
        print(args , kwargs)
        pk = kwargs.get('pk')
        # getting the value of the key pk form the kwargs ( dictionary )

        if pk is not None : 
            return self.retrieve(request , *args  , **kwargs)
        return self.list(request  , *args , **kwargs)
        # returning the list of the requet , args and kwargs 




    # get post() : http -> post 

product_mixin_view  = ProductMixinView.as_view()