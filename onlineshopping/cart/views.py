<<<<<<< HEAD
<<<<<<< HEAD
# from django.shortcuts import render,get_object_or_404,redirect
# from .models import Product
# from cart.models import Order,OrderItem
# # Create your views here.
# def add_to_card(request,slug):
#     item=get_object_or_404(Product,slug=slug)
#     order_item=OrderItem.objects.Create(item=item,ordered=False)
#     order=Order.objects.Create(user=request.user)
#     order.add_to_card(order_item)
#     return redirect("myshopping:product",kwargs={
#         'slug':slug
#     })
=======
=======
>>>>>>> TestBranch4
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from myshopping.models import Product
from cart.models import Cart
from cart.models import Order
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView
<<<<<<< HEAD

# Add to Cart View

def add_to_cart(request, product_id):
    item = get_object_or_404(Product, product_id=product_id)
=======
from myshopping import urls

# Add to Cart View

def add_to_cart(request, product_name):
    item = get_object_or_404(Product, product_name=product_name)
>>>>>>> TestBranch4
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
<<<<<<< HEAD
        if order.orderitems.filter(item__product_id=item.product_id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("mainapp:list")
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("mainapp:list")
=======
        if order.orderitems.filter(item__product_name=item.product_name).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("products")
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("products")
>>>>>>> TestBranch4
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
<<<<<<< HEAD
        return redirect("mainapp:list")

# Remove item from cart

def remove_from_cart(request, product_id):
    item = get_object_or_404(Product, product_id=product_id)
=======
        return redirect("products")

# Remove item from cart

def remove_from_cart(request, product_name):
    item = get_object_or_404(Product, product_name=product_name)
>>>>>>> TestBranch4
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
<<<<<<< HEAD
        if order.orderitems.filter(item__product_id=item.product_id).exists():
=======
        if order.orderitems.filter(item__product_name=item.product_name).exists():
>>>>>>> TestBranch4
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
<<<<<<< HEAD
            return redirect("mainapp:list")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("mainapp:list")
=======
            return redirect("products")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("products")
>>>>>>> TestBranch4
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:list")

<<<<<<< HEAD
<<<<<<< HEAD
# class Home(ListView):
#     model = Product
#     template_name = 'products/home.html'
>>>>>>> TestBranch3
=======
=======
>>>>>>> TestBranch4
# Cart View

def CartView(request):

    user = request.user

    carts = Cart.objects.filter(user=user)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        order = orders[0]
        return render(request, 'cart/home.html', {"carts": carts, 'order': order})
		
    else:
        messages.warning(request, "You do not have an active order")
<<<<<<< HEAD
        return redirect("core:list")
>>>>>>> TestBranch3
=======
        return redirect("core:products")
>>>>>>> TestBranch4
