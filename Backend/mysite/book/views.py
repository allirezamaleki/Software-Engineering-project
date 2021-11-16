from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    book_list = Product.objects.all()
    return HttpResponse(book_list)

def product(request):
    return HttpResponse("This is an item")