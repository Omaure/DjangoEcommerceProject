from django.contrib import admin
from django.urls import path
from myshopping import views
from . import views

urlpatterns=[
    path('', views.product_list, name='list'),
]