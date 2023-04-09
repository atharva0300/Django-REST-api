from django.urls import path

# importing views 
from .views import api_home

urlpatterns = [
    path('' , api_home  , name = 'api_home')   # this is going to be localhost:8000/api/
]