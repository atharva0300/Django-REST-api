# creating the urls.py for mapping all the urls for the api app
from django.urls import path 
from .views import api_home

# importing the auth token 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('' , view = api_home),  # http://localhost:8001/api
    path('auth/' , view = obtain_auth_token)
]