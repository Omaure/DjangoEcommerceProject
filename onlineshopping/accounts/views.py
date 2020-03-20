from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from accounts.forms import EditProfileForm
# ProfileUpdateForm
from django.contrib import messages


# Create your views here.
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm,UserRegisterForm
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
def details(request):
    userdetails = UserProfile.objects.all()
    context = {'object_list': userdetails}
    print(context)
    return render(request, "userDetails.html", context)


def delete_profile(request):
    user = request.user
    user.is_active = False
    user.save()
    messages.success(request, 'Profile successfully disabled.')
    return redirect('/')


def userpage(request):
    args = {'user': request.user}
    return render(request, 'userpage.html', args)

def editprofile(request):
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid() and p_form.is_valid():
            form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('/userpage')
    else:
        form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
        args = {
            'form': form,
            'p_form': p_form
        }
        return render(request, 'edit_profile.html', args)
