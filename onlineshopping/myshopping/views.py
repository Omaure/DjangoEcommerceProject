from django.shortcuts import render
from django.http import HttpResponse
from myshopping.models import Product, Category
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def index(request, **Kwargs):
    return render(request, 'index.html')


def product_list(request):
    object_list = Product.objects.all()
    context = {'object_list': object_list}
    print(context)
    return render(request, "index.html", context)
