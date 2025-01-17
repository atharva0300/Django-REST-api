from django.shortcuts import render

# Create your views here.
# designing the api endpoint view 
from django.http import JsonResponse , HttpResponse

# to convert the bytestring to json 
import json

# importing product model
from products.models import Product

# to convert the api_vieew to a REST framework API view 
# we import 2 things -> Response and APIView 
# and apply to it
from rest_framework.response import Response
from rest_framework.decorators import api_view

# model to dict 
from django.forms.models import model_to_dict

# importing serializers 
from products.serializers import ProductSerializer


@api_view(['GET', 'POST'])
# the api_view(['GET']) -> means that only GET method is allowed 
# the api_view(['POST']) -> means that only POST method is allowed 
# the api_view(['GET, POST']) -> means that only GET and POST method is allowed 
def api_home(request , *args , **kwargs) :
    """
    
    DRF API view
    
    """

    if request.method=='POST' : 
        print('inside post request')
        # handling post requests
        serializer = ProductSerializer(data = request.data)
        # passing the request data in the serializer 

        if serializer.is_valid(raise_exception=True) : 
            print('serializer is valid')
            # checking if it matches if this data is formatted

            # saving the serialized data 
            serializer.save()
            # this will save the instance
            # without saving tteh serializer, the instance methods and properties do not get applied 
            # ie -> it will show the data for all the selected fields 
            # it has all the other data for us like -> my_discount, get_discount , sale_price , content , price -> when when 
            # we haven't passed these values 
            # obtaining the saved instance => instance = serializer.save()
            data = serializer.data
            print(serializer.data)


            return Response(data , status = 200)
        
        return Response({'invalid' : 'Not good Data'} , status = 400)
    

    #model_data = Product.objects.all().order_by("?").first()

    instance = Product.objects.all().order_by("?").first()

    data = {} 

    if instance : 
        """
        data['id'] = model_data.id  # adding the id provided by the model ( this is not developer defined and automatically created by Django )
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

        """
        # model instance ( model_data )
        # turn a python dict
        # serialization
        # return the data to the client 

        # using model_to_dict 
        # data = model_to_dict(instance , fields =['id' , 'title' ,  'price' , 'sale_price'])
        # which fields to convert to dict is mentioned in fields 
        # the sale_price does not get added by default

        # httpresponse => accepts a string 
        # jsonresponse => accepts a json data

        # converting the json to string 
        # json_data_str = json.dumps(data)

        # BY USING SERIALIZERS ( ProductSerializer )
        data = ProductSerializer(instance).data

        return Response(data)
 
    # we use Response(data) -> when using REST API 
    # we use JsonResponse(data) -> when we want tp send an object but it is not a REST API
    
    # return HttpResponse(json_data_str , headers = {'content-type' : 'application/json'})

    # to change the http response to json data -> HttpResponse(data , headers = {'content-type' : 'application/json'})
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