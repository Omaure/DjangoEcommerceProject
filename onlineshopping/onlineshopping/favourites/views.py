from django.shortcuts import render
from django.shortcuts import get_object_or_404
from myshopping.models import Product
from favourites.models import Favourites
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView
from myshopping import urls


# Create your views here.

# Add to Fav View

def add_to_fav(request, product_name):
    item = get_object_or_404(Product, product_name=product_name)

    condition = Favourites.objects.filter(favitem=item)
    if condition.exists():
        messages.info(request, "This item is already in your Favourites")
        return redirect("products")
    else:
        Favourites.objects.get_or_create(
            favitem=item,
            user=request.user
        )
        messages.info(request, "This item has been added to your Favourites")
        return redirect("products")


# Remove item from Fav

def remove_from_fav(request, product_name):
    item = get_object_or_404(Product, product_name=product_name)
    fav_qs = Favourites.objects.filter(user=request.user, favitem=item)
    if fav_qs.exists():
        fav = fav_qs[0]
        fav_qs.delete()
    return redirect("products")


# Fav View

def FavView(request):
    user = request.user
    favs = Favourites.objects.filter(user=user)
    if favs.exists():
        return render(request, 'fav/home.html', {"favs": favs})

    else:
        messages.warning(request, "You do not have any Favourites")
        return redirect("products")