from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins, permissions, authentication

from .models import Product
from .serializers import ProductSerializer

# importing the api_view and the Response to convert the normal Django APi to the REST API 
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.shortcuts import get_object_or_404

# importing the custom permissions
from api.permissions import IsStaffEditorPermission
# importing the custom authentication over here
from api.authentication import TokenAuthentication 

# importing the permission mixin 
from api.mixins import StaffEditorPermissionMixin


# creating a ProductDetailAPIView
class ProductDetailAPIView(generics.RetrieveAPIView) : 
    
    # get the queryset 
    queryset = Product.objects.all()

    # creating a product serializer
    serializer_class = ProductSerializer

    # lookup_field = 'pk'
    # Product.objects.get(pk = 2)

    #permission_classes = [permissions.IsAuthenticated]
    # permissions.IsAuthenticated -> if not authenticated -> cannot use the get or the post method 
    # permissions.IsAuthenticatedOrReadOnly -> if not authenticated -> can only use the get method and not the post method

    authentication_classes = [authentication.SessionAuthentication]
    # provides session authentication


product_detail_api_view = ProductDetailAPIView.as_view()
# this will convert the class api view as a Django understandable view 


class ProductListCreateAPIView(generics.ListCreateAPIView , StaffEditorPermissionMixin) : 
    # ListCreateAPI View is a combination of both create and list APi View 
    # Create API View is called when -> the request.method is 'POST' request -> you are trying to create a new Product
    # List API View is called when -> the request.method is a 'GET' request -> you are trying to get the list of all the Products


    queryset = Product.objects.all()

    serializer_class = ProductSerializer
    # getting the Product Serializer 


    permission_classes = [IsStaffEditorPermission , permissions.IsAdminUser]
    # permissions.IsAuthenticated -> if not authenticated -> cannot use the get or the post method 
    # permissions.IsAuthenticatedOrReadOnly -> if not authenticated -> can only use the get method and not the post method
    # IsStaffEditorPermission -> custom made permissions in the permissions.py file

    authentication_classes = [authentication.SessionAuthentication , TokenAuthentication]
    # provides session authentication
    # this gives the permission to create new item in the browser. ( if there is any create form )
    # adding token authentication

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



class ProductListAPIView(generics.ListAPIView , StaffEditorPermissionMixin) : 
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




# creating a ProductDetailAPIView
class ProductUpdateAPIView(generics.UpdateAPIView) : 
    
    # get the queryset 
    queryset = Product.objects.all()

    # creating a product serializer
    serializer_class = ProductSerializer

    permission_classes = [permissions.DjangoModelPermissions]
    # This will only give permissions to the staff user which are given by the superuser
    

    lookup_field = 'pk'
    # specifying the lookup field

    def perform_update(self , serializer) : 
        instance = serializer.save()
        # saving the serializer

        if not instance.content : 
            instance.content = instance.title 
            # if the content it blank, then set it the same as the title



product_update_view = ProductUpdateAPIView.as_view()
# this will convert the class api view as a Django understandable view 



# creating a ProductDetailAPIView
class ProductDestroyAPIView(generics.DestroyAPIView) : 
    
    # get the queryset 
    queryset = Product.objects.all()

    # creating a product serializer
    serializer_class = ProductSerializer

    lookup_field = 'pk'

    def perform_destroy(self , instance) : 
        # instance 

        # destroying ( deleting ) the item
        super().perform_destroy(instance)
    


product_destroy_view = ProductDestroyAPIView.as_view()
# this will convert the class api view as a Django understandable view 


class ProductMixinView(mixins.CreateModelMixin , mixins.ListModelMixin , mixins.RetrieveModelMixin , generics.GenericAPIView  ) : 

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    lookup_field = 'pk'


    # uses mixins.REtrieveModelMixin 
    def get(self , request , *args, **kwargs) :     # Http -> get 
        print(args , kwargs)

        # just keeping the pk 
        pk = kwargs.get('pk')

        if pk is not None : 
            return self.retrieve(request , *args , **kwargs)
            
            # returns the by defauly method by Django -> .retrieve
        
        # uses mixins.ListModelMixin
        return self.list(request , *args , **kwargs)
        # returns the by defauly method by Django -> .list
   
    

    # uses mixins.RetrieveModelMixin
    def post(self , request , *args , **kwargs)  : # HTTP -> post
        return self.create(request , *args , **kwargs)
        # returns the by defauly method by Django -> .create

    # uses mixins.CreateModelMixin
    def perform_create(self ,serializer) :
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        # checking if the content is there or not ? 
        if content is None : 
            content = "This is a single view doing cool stuff"
        

        serializer.save(content = content) 

        # send a signal here ( a Django here )

product_mixin_as_view = ProductMixinView.as_view()