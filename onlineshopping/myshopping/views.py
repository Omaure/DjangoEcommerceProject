<<<<<<< HEAD
from django.http import HttpResponse
from myshopping.models import Product, Category, User, UserProfile
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def index(request, **Kwargs):
    return render(request, 'index.html')


def details(request):
    userdetails = UserProfile.objects.all()
    context = {'object_list': userdetails}
    print(context)
    return render(request, "userDetails.html", context)


def product_list(request):
    object_list = Product.objects.all()
    context = {'object_list': object_list}
    print(context)
    return render(request, "index.html", context)
=======
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q # new

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


def displayProductData(request,productName):
    p=Product.objects.get(product_name=productName)
    s =p.image1.path
    context = {
        
        'product': Product.objects.get(product_name=productName)
    }

    return  render(request,"productbyname.html",context)  
    
class SearchResultsView(ListView):
    model = Product
    template_name = 'searchresults.html'
    

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(
            Q(product_name__icontains=query) | Q(product_price__icontains=query)
        )
        return object_list



def filter(request):
    qs = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    product_name_query = request.GET.get('q')
    cat_name_query = request.GET.get('q')
    brand_name_query = request.GET.get('q')
    if (qs.filter(product_name__icontains=product_name_query)|qs.filter(product_price__icontains=product_name_query)):
        qs = qs.filter(product_name__icontains=product_name_query ) | qs.filter(product_price__icontains=product_name_query )

    elif (categories.filter(cat_name__icontains= cat_name_query) ):
        qs = categories.filter(cat_name__icontains= cat_name_query)
    else: 
        qs=  brands.filter(name__icontains=brand_name_query)  
    return qs

def BootstrapFilterView(request):
    qs = filter(request)
    context = {
        'queryset': qs,
        'categories':Category.objects.all(),
        'subCat':SubCategory.objects.all(),
        'brands':Brand.objects.all(),
        'products':Product.objects.all()
      
    }
    return render(request, "searchresults.html", context) 
    

>>>>>>> TestBranch4
