from django.urls import path

from .views import product_detail_api_view , product_list_create_api_view , product_alt_view, product_update_view , product_destroy_view, product_mixin_as_view


urlpatterns = [
    path('' , product_list_create_api_view , name = 'product-list'),
    path('mixins/' , product_mixin_as_view),
    path('<int:pk>/' , product_detail_api_view , name = 'product-detail'),
    path('<int:pk>/update/' , product_update_view , name = 'product-edit'),
    path('<int:pk>/destroy/' , product_destroy_view),
    path('alt/' , product_alt_view)
]