from django.urls import path

from . import views

urlpatterns = [
    path('' , views.product_create_api_view , name = 'product_create_api_view'),
    path('<int:pk>/update/' , views.product_update_view),
    path('<int:pk>/delete/' , views.product_destroy_view),
    path('<int:pk>/' , views.product_detail_view  , name = 'product_detail_api_view'),
    path('mixins/' , views.product_mixin_view , name = 'product_mixin_view'),
    path('mixins/<int:pk>/' , views.product_mixin_view , name = 'product_mixin_view')

]