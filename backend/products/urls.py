from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/' , views.product_detail_view  , name = 'product_detail_api_view')
]