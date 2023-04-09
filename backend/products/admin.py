from django.contrib import admin

from .models import Product

# Register your models here.
# adding hte product model to the admin
admin.site.register(Product)