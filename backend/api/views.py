from django.shortcuts import render

# importing the json package 
import json

# importign the json response library inbuilt in djangp
from django.http import JsonResponse

# importing the Product model 
from products.models import Product\

# importing a library that converts a model to a dictionry 
from django.forms.models import model_to_dict

# Create your views here.

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


def api_home2(request , *args , **kwargs) : 

    model_data = Product.objects.all().order_by("?").first()

    data = {} # the empty dictionary 
    if model_data : 
        # if there is any data in the model_data
        data['id'] = model_data.id
        data['title'] = model_data.title 
        data['content'] = model_data.content
        data['price'] = model_data.price

        # get a model instance 
        # turn it into a python dictionry 
        # return Json to my client

        data2 = model_to_dict(model_data , fields = ['id' , 'title' , 'content' , 'price'])
        # all the fields we want the API to respond with
        return JsonResponse(data2)
    
    else : 
        return JsonResponse({"message" : "There is no data"})
    
    # JsonResponse -> accepts a json object 
    # HttpResponse -> accepts a string
    
    # to convert the dictionary( object )to a string 
    # use json.dumps(data)
    # json_data_str = json.dumps(data)

    