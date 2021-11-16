from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Item(models.Model):
    
    
    def __str__(self):
        return self.item_name
    
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://www.kindpng.com/picc/m/725-7251301_book-cover-placeholder-hd-png-download.png")
    

