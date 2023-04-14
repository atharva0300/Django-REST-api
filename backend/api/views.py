from django.shortcuts import render

# importing the json package 
import json

# importign the json response library inbuilt in djangp
from django.http import JsonResponse

# importing the Product model 
from products.models import Product

# importing a library that converts a model to a dictionry 
from django.forms.models import model_to_dict

# importing the response class from the dango rest framework 
from rest_framework.response import Response
from rest_framework.decorators import api_view
# api_view is a decorator

# importing the Product Serializer
from products.serializers import ProductSerializer


# Create your views here.

# mentioning that it is an API view
@ api_view(['POST' , 'GET'])
# listing all the methods that we require we mention in an array        
def api_home(request , *args , **kwargs) :
    # request -> http request instance from django 
    # print(dir(request))       # this will give the body of the request
    # request.body

    body = request.body     # getting the bytestring of JSON data
    print(body)

    data = {}   # empty dictionary
    try : 
        data = json.loads(body)     # takes a string of JSON data and turns it into a dictionary
    except : 
        pass

    print(data)

    # adding the data 
    #data['headers'] = request.headers       # storing the data in the headers key 
    print(request.headers)
    # http Headers are not JSON serializable 
    data['headers'] = dict(request.headers)
    # so, we convert the headers to a dictionary
    data['content_type'] = request.content_type     # getting the content_type and storing for the key content_type

    # get the URL query parameter 
    print(request.GET)          # this will obtain the abs = 123 value which we had passed as the parameter

    # get the PSOT parametre
    #print(request.POST)
    data['params'] = request.GET
    # request.GET is already JSON serializable

    return JsonResponse(data)




# mentioning that it is an API view
@api_view(['POST' , 'GET'])
# this allows only the POST method to access the function 
# listing all the methods that we require we mention in an array       
def api_home2(request , *args , **kwargs) : 
    """
    
    DRF API View

    """

    #if request.method!='POST': 
    #    return Response({'detail' : 'GET not allowed'} , status=405)
    #    we return a json response along with the status code
    

    data = request.data 
    # getting the data from the request 


    instance = Product.objects.all().order_by("?").first()
    # the instance is the model data

    data = {} # the empty dictionary 
    if instance : 
        # if there is any data in the model_data
        data['id'] = instance.id
        data['title'] = instance.title 
        data['content'] = instance.content
        data['price'] = instance.price

        # get a model instance 
        # turn it into a python dictionry 
        # return Json to my client

        data2 = model_to_dict(instance , fields = ['id' , 'title' , 'content' , 'price' , 'sale_price'])
        # adding the sale_price does not show int he API result 
        # this is one of the reason to use serializer

        data3 = ProductSerializer(instance).data
        # getting the contents ( all the data ) in a serialized way 
        # this will also show the sale price and get discount

        # all the fields we want the API to respond with




        return JsonResponse(data3)
    
    else : 
        return JsonResponse({"message" : "There is no data"})
    
    # JsonResponse -> accepts a json object 
    # HttpResponse -> accepts a string
    
    # to convert the dictionary( object )to a string 
    # use json.dumps(data)
    # json_data_str = json.dumps(data)


    """
    
    serializer = ProductSerializer(data = request.data)
    # it makes sure that the data that is being sent in ( injeced )
    # is formatted

    if serializer.is_valid() : 
    # this checks it the data is formatted
        print(serializer.data)
        data = serializer.data
        return Response(data)
        
        # if the error -> data is not serializable occurs, then we will have to return 
        return Response(serializer.data)
    
    """
    