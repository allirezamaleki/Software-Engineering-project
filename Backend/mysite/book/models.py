from django.db import models

# Create your models here.
class Product(models.Model):
    
    def __str__(self):
        return self.product_name
    
    product_name = models.CharField(max_length=200)
    product_desc = models.CharField(max_length=200)
    product_price = models.IntegerField()