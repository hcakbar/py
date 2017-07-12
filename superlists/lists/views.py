from django.shortcuts import redirect, render
from lists.models import Item, List
from django.db import models
from lists.models import Item

def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')

class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
