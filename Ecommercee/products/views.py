from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from products.models import Product

class Home(ListView):
    model = Product
    template_name = 'products/home.html'