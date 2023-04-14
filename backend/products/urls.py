from django.urls import path

from .views import product_detail_api_view , product_create_api_view


urlpatterns = [
    path('' , product_create_api_view),
    path('<int:pk>/' , product_detail_api_view),
]