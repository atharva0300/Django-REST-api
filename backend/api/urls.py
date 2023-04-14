# creating the urls.py for mapping all the urls for the api app
from django.urls import path 
from .views import api_home

urlpatterns = [
    path('' , view = api_home)  # http://localhost:8001/api
]