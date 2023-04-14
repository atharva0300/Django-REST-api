from django.db import models

# Create your models here.
class Product(models.Model) :
    # pk by default
    title = models.CharField(max_length=100)
    content = models.TextField(blank = True , null = True )
    price = models.DecimalField(max_digits=15 , decimal_places=2 ,default=99.99)

    # creating a property 
    @property
    def sale_price(self) : 
        n = float(self.price) * 0.8
        temp = "%.2f" %n
        return temp
    
    # instance function
    def get_discount(self) : 
        return "122"