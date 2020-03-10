from django.contrib import admin
from django.urls import path, include
from myshopping import views
from . import views

urlpatterns = [
    path('', views.product_list, name='list'),
    path('accounts/', include('allauth.urls')),
]
