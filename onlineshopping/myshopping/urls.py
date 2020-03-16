from django.contrib import admin
from django.urls import path
from myshopping import views
from . import views
from cart.views import add_to_cart, remove_from_cart
app_name= 'mainapp'

urlpatterns=[
    # ex: /library/
    # path('', views.index, name='index'),
    path('', views.product_list, name='list'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]