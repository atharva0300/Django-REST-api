from django.shortcuts import render

# Create your views here.
# designing the api endpoint view 
from django.http import JsonResponse

# to convert the bytestring to json 
import json

# importing product model
from products.models import Product

def api_home(request , *args , **kwargs) :

    model_data = Product.objects.all().order_by("?").first()

    data = {} 

    if model_data : 
        data['id'] = model_data.id  # adding the id provided by the model ( this is not developer defined and automatically created by Django )
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

        # model instance ( model_data )
        # turn a python dict
        # serialization
        # return the data to the client 

    return JsonResponse(data)

    """
    
    # request -> HttpRequest -> Django
    # print(dir(request))
    # request.body
    body = request.body     # json data ( bytestring of json data )
    print(body) # in bytestring
    data = {}    
    try : 
        data = json.loads(body)
    except : 
        pass

    print(data) 
    data['headers'] = dict(request.headers)  # request.META
    # the request.headers is not serializable 
    # so we convert it into a dict
    data['content_type'] = request.content_type     # getting the content type of the request data
    print(data['content_type'])
    print(data['headers'])

    print(request.GET)  # displayed the query parameters of the url 
    data['params'] = dict(request.GET)

    return JsonResponse(data) 
    # returning back the received data 
    # return JsonResponse(data)

    """