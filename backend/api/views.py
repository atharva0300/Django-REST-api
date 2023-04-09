from django.shortcuts import render

# importing the json package 
import json

# importign the json response library inbuilt in djangp
from django.http import JsonResponse

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