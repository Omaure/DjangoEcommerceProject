from django.contrib import admin
from django.urls import path
from myshopping import views
from . import views

urlpatterns=[
    # path('', views.category_list, name='list'),
    path('', views.Data_list, name='sublist'),
    path('products/', views.products, name='products'),
    path('productbyname/<productName>/',views.displayProductData,name='productbyname'),
    path('search' , views.search , name='search'),
]