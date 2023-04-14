#from django import forms

# to cvonert the forms.py to serializers.py 
# we just add and replacea  few things 

# import serializers
from rest_framework import serializers 

from .models import Product

from rest_framework.reverse import reverse
# this allows other urls ( changed urls )

class ProductSerializer(serializers.ModelSerializer) : 

    my_discount = serializers.SerializerMethodField(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(
        view_name = 'product-detail',
        lookup_field = 'pk',
        )
    class Meta : 
        model = Product
        fields = [
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',

            # we write out sale_price over here
            'sale_price',

            # we can add instance method or a property in the serializer
            # which otherwise could not be used when added in models.py

            # adding instance method get_discount 
            'get_discount',

            # if we want to call the 'get_discount' as just 'my_discount'
            # then by just changing the name to 'discount' we get an error
            # 'my_discount'

            # after adding : discount = serializers.SerializerMethodField(read_only = True)
            'my_discount'
        ]

    # the funciton name can only be -> 'get_<something>_discount'
    # so that Django can identify the correct function 
    def get_my_discount(self , obj) : 
        
        if not hasattr(obj , 'id') : 
            # checking if the 'id' attribute is received by the client 
            return None
        
        if not isinstance(obj , Product) : 
            # checking if the instance is the child instance of the Product model or not
            return None
        
        try : 
            print(obj.id)
            # if we had a obj.user -> we can grab that 
            # or obj.foreignkey -> we can grab that
            return obj.get_discount()
        except : 
            pass 

    
    def get_edit_url(self , obj) : 

        # return f"/api/products/{obj.pk}/"

        request = self.context.get('request')   # self.request

        if request is None : 
            return None
        
        # use it as an argument
        return reverse("product-detail" , kwargs = {'pk' : obj.pk} ,  request = request )
        # pk is the name of the keyword argument
        