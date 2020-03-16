<<<<<<< HEAD
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from myshopping import views
from . import views
<<<<<<< HEAD
from myshopping.views import login_view,logout_view,register_view
=======
from cart.views import add_to_cart, remove_from_cart
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
>>>>>>> TestBranch4
=======
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
]
>>>>>>> TestBranch3
