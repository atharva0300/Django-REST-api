from django import forms 

# we import serializers from rest framework 
from rest_framework import serializers


from .models import Product

class ProductSerializer(serializers.ModelSerializer) : 
    # inherit the ModelSerializer
    # so that we can display the sale price ( which is a decorator function value and not an actual field )

    # allowing the discount to point to get_discount 
    my_discount = serializers.SerializerMethodField(read_only = True )
    # set the read_only to True 
    
    class Meta : 
        model = Product

        fields = ['title' , 'content' , 'price' , 'sale_price' , 'my_discount']
        # changing the field name get_discount to some other name 
        # without chanigng the same name in the model.py file 
        # will give an error 
        # but we can do this the other way
    

    # creating a function that will point the my_discount to the get_discount 
    def get_my_discount(self , obj) :
        print(obj.id)
        # printing the id of the object ( the record )


        return obj.get_discount()
        # this will make it point 

        # NOTE that any other name like just 'discount' will get error 
        # it should be <str>_discoount because it is similar to get_discount
