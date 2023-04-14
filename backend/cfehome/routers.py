# creating this file to separate the viewset and the views 

# importing the routers 
from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductGenericViewSet

router = DefaultRouter()
router.register('products-abc' , ProductGenericViewSet, basename = 'products')

# router.register('products-cba' , ProductViewSet , basename = 'products')

print(router.urls)

# the router will get the location of a webpage into some other location ( url )
urlpatterns = router.urls

