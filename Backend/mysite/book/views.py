from django import template
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ItemForm
from .models import Item
from django.template import context, loader


# Create your views here.

def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template("book/index.html")
    context = {
        'item_list': item_list,
    }
    return render(request, 'book/index.html', context)
    # return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse("These are the items.")

def detail(request, item_id):
    item = Item.objects.get(pk = item_id)
    context = {
        'item': item,
    }
    # return HttpResponse("This is item no/id: %s" % item_id)
    return render(request, 'book/detail.html', context)


def create_item(request):
    form = ItemForm(request.POST or None)
    context = {
        'form': form,
    }
    
    if form.is_valid():
        form.save()
        return redirect('book:index')
    
    return render(request, 'book/item-form.html', context)

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    
    context = {
        'form': form,
        'item': item,
    }
    
    if form.is_valid():
        form.save()
        return redirect('book:index')
    
    return render(request, 'book/item-form.html', context)


def delete_item(request, id):
    item = Item.objects.get(id = id)
    context = {
        'item': item,
    }
    
    if request.method == 'POST':
        item.delete()
        return redirect('book:index')
    
    return render(request, 'book/item-delete.html', context)