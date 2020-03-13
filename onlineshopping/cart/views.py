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
