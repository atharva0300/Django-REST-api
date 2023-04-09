from django.db import models

# Create your models here.
class Product(models.Model) :
    title = models.CharField(max_length= 100)
    content = models.TextField(blank = True , null = True )
    price = models.DecimalField(max_digits=15 , decimal_places=2 , default = 99.99) 
    # the title , content , price are the fields of the model 


    # defining a new dcorator
    @property 
    def sale_price(self) : 
        result = float(self.price) * 0.8
        return (result)
    
    def get_discount(self) : 
        return "122"