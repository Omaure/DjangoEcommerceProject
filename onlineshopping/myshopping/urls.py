from django.contrib import admin
from django.urls import path
from myshopping import views
from . import views
from .views import SearchResultsView,BootstrapFilterView
urlpatterns=[
    # path('', views.category_list, name='list'),
    path('', views.Data_list, name='sublist'),
    path('products/', views.products, name='products'),
    path('productbyname/<productName>/',views.displayProductData,name='productbyname'),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/', views.BootstrapFilterView, name='search_results'),
]