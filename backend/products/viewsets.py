from rest_framework import viewsets
# importing viewsets 

from .models import Product
from .serializers import ProductSerializer

from rest_framework import mixins


class ProductViewSet(viewsets.ModelViewSet) :
    '''
    
    get -> list -> queryset 
    get -> retrieve -> Product Instance detail view 
    post -> create -> New Instance 
    put -> Update 
    patch -> Partial Update 
    delete -> destroy
    
    '''
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    lookup_field = 'pk' # default 

    # after creating the viewset 
    # bring it in the router 


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet) :
     
    '''
    
    get -> list -> queryset 
    get -> retrieve -> Product Instance detail view 
    post -> create -> New Instance 
    put -> Update 
    patch -> Partial Update 
    delete -> destroy
    
    '''
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    lookup_field = 'pk' # default 

    # after creating the viewset 
    # bring it in the router 


