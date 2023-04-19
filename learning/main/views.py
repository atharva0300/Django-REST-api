from django.shortcuts import render

from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf  import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Typing
from .serializers import TypingSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
#@api_view(['GET' ,'POST']) -> for function based views only 
class TypingList(APIView) :
    """
    
    List of all the Typing code snippets 

    """

    def get(self , request , format = None ) : 
        items = Typing.objects.all()
        serializer = TypingSerializer(items , many = True )
        return Response(serializer.data)
    
    def post(self , request , format = None ) :
        serializer = TypingSerializer(data = request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


    """

    for function based views only -> 


    if request.method=='GET' : 
        items = Typing.objects.all()
        serializer = TypingSerializer(items,  many = True)
        return JsonResponse(serializer.data , safe=False)
    

    if request.method=='POST' : 
        
        # parse the data 
        data = JSONParser().parse(request)
        serializer = TypingSerializer(data =data)

        if serializer.is_valid() : 
            serializer.save()
            return JsonResponse(serializer.data , status = 200)
        
        # else case 
        return JsonResponse(serializer.errors , status = 400)
    
    return HttpResponse("This is response")
    """

#@api_view(['GET']) -> for function based views only
class TypingDetail(APIView) : 

    def get_object(self , pk) : 
        try : 
            return Typing.objects.get(pk = pk)
        
        except Typing.DoesNotExist :
            return Http404

    def get(self , request , pk , format = None ) : 
        item = self.get_object(pk)
        # getting the object
        serializer = TypingSerializer(item)
        return Response(serializer.data)
    

    """

    for function based vies only -> 

    try : 
        item = Typing.objects.get(pk =pk)
    except Typing.DoesNotExist :
        return HttpResponse(status = 404)

    if request.method == 'GET' :
        serializer = TypingSerializer(item) 
        return JsonResponse(serializer.data)
    """