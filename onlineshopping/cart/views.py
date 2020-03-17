from django.shortcuts import render
from django.shortcuts import get_object_or_404
from myshopping.models import Product
from cart.models import Cart
from cart.models import Order
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView

# Add to Cart View

def add_to_cart(request, product_id):
    item = get_object_or_404(Product, product_id=product_id)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__product_id=item.product_id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("mainapp:list")
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("mainapp:list")
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("mainapp:list")

# Remove item from cart

def remove_from_cart(request, product_id):
    item = get_object_or_404(Product, product_id=product_id)
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
        if order.orderitems.filter(item__product_id=item.product_id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("mainapp:list")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("mainapp:list")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:list")

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
        return redirect("core:list")