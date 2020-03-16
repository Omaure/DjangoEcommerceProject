from django.http import HttpResponse
from myshopping.models import Product, Category, User, UserProfile
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegisterForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')


def index(request, **Kwargs):
    return render(request, 'index.html')


def details(request):
    userdetails = UserProfile.objects.all()
    context = {'object_list': userdetails}
    print(context)
    return render(request, "userDetails.html", context)


def product_list(request):
    object_list = Product.objects.all()
    context = {'object_list': object_list}
    print(context)
    return render(request, "index.html", context)
