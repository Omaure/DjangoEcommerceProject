from django.contrib import admin
from django.urls import path
from myshopping import views
from . import views

urlpatterns=[
    # ex: /library/
    # path('', views.index, name='index'),
    path('', views.product_list, name='list'),
]