from django.shortcuts import render
from django.http import HttpResponse
from myshopping.models import Product,Category,SubCategory,Brand
# 
# ,Brand
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def index(request,**Kwargs):
    return render(request, 'index.html')  

def category_list(request):
    cat_list= Category.objects.all()
    context= {'cat_list': cat_list}
    
    return render(request, "index.html", context) 

def Data_list(request):
    cat_list= Category.objects.all()
    subcat_list= SubCategory.objects.all()
    brand_list=Brand.objects.all()
    product_list=Product.objects.all()
    context= {'cat_list': cat_list,'subcat_list': subcat_list,'brand_list':brand_list,'product_list':product_list}
    print(context)
    return render(request, "index.html", context)     


def products(request):
    context = {
        
        'products': Product.objects.all()
    }
    return render(request, "products.html", context)