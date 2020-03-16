from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from myshopping import views
from . import views
from myshopping.views import login_view,logout_view,register_view

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
    path('accounts/login/', login_view),
    path('accounts/signup/', register_view),
    path('accounts/logout/', logout_view)

    # url(r'^accounts/signup/$', signup),  # signup url
    # url(r'^accounts/login/$', login),  # login url
]
