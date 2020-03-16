<<<<<<< HEAD
# from django.contrib import admin

# # Register your models here.

# # Register your models here.
# from .models import Order,OrderItem
# admin.site.register(Order)
# admin.site.register(OrderItem)
=======
from django.contrib import admin
from cart.models import Cart,Order

admin.site.register(Cart)
admin.site.register(Order)
>>>>>>> TestBranch3
