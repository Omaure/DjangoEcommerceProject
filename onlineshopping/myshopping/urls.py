<<<<<<< HEAD
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from myshopping import views
from . import views
<<<<<<< HEAD
<<<<<<< HEAD
from myshopping.views import login_view,logout_view,register_view
=======
from cart.views import add_to_cart, remove_from_cart
=======
from cart.views import CartView, add_to_cart, remove_from_cart
>>>>>>> TestBranch3
app_name= 'mainapp'
>>>>>>> TestBranch3

from allauth.account.views import LoginView, SignupView

#
# class Lvx(LoginView):
#     template_name = "login.html"
#
#
# login = Lvx.as_view()
#
#
# class Suvx(SignupView):
#     template_name = "signup.html"
#
#
# signup = Suvx.as_view()

urlpatterns = [
    path('', views.product_list, name='list'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('accounts/login/', login_view),
    path('accounts/signup/', register_view),
    path('accounts/logout/', logout_view)

    # url(r'^accounts/signup/$', signup),  # signup url
    # url(r'^accounts/login/$', login),  # login url
]
=======
from django.contrib import admin
from django.urls import path
from myshopping import views
from django.conf.urls import url, include
from . import views
from .views import SearchResultsView, BootstrapFilterView
from accounts.views import login_view, register_view, logout_view
from cart.views import CartView, add_to_cart, remove_from_cart
from myshopping.views import products
from myshopping import urls

urlpatterns = [

    path('', views.Data_list, name='sublist'),
    path('products/', products, name='products'),
    path('productbyname/<productName>/', views.displayProductData, name='productbyname'),
    # path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/', views.BootstrapFilterView, name='search_results'),
<<<<<<< HEAD
]
>>>>>>> TestBranch4
=======
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]
>>>>>>> TestBranch3
=======
    path('cart/<product_id>', add_to_cart, name='cart'),
    path('remove/<product_id>', remove_from_cart, name='remove-cart'),
    path('cartview/', CartView, name='cart-home'),
]
>>>>>>> TestBranch3
=======
    path('accounts/login/', login_view),
    path('accounts/signup/', register_view),
    path('accounts/logout/', logout_view),
    path('products/cart/<product_name>', add_to_cart, name='cart'),
    path('products/remove/<product_name>', remove_from_cart, name='remove-cart'),
    path('products/cartview/', CartView, name='cart-home'),
    path('productbyname/$/cart/<product_name>', add_to_cart, name='cart'),

]
>>>>>>> TestBranch4
