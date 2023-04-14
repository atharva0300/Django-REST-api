#from django import forms

# to cvonert the forms.py to serializers.py 
# we just add and replacea  few things 

# import serializers
from rest_framework import serializers 

from .models import Product

class ProductSerializer(serializers.ModelSerializer) : 

    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta : 
        model = Product
        fields = [
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

    
