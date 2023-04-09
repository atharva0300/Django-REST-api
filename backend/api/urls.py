from django.urls import path , include

# importing views 
from .views import api_home , api_home2

urlpatterns = [
    path('' , api_home  , name = 'api_home'),   # this is going to be localhost:8000/api/
    path('api_home2/' , api_home2 , name = 'api_home2')

    # adding the url of another app 
]