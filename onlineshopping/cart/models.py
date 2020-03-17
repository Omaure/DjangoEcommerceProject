<<<<<<< HEAD
# from __future__ import unicode_literals
# from django.db import models
# from myshopping.models import Product
# # Create your models here.


# class OrderItem(models.Model):
#       item=models.ForeignKey(Product,on_delete=models.CASCADE)
#       ordered = models.BooleanField(default=False)
#       quantity = models.IntegerField(default=1)

# class Order(models.Model):
#       ref_code=models.CharField(max_length=15)
#       is_ordered=models.BooleanField(default=False)
#       items=models.ManyToManyField(OrderItem)
#       date_orderd=models.DateTimeField(auto_now=True)
#       def get_cart_items(self):
#           return self.items.all()
#       def get_cart_total(self):
#           return sum([items.product.product_price for item in self.items.all()])
#       def __str__(self):
#           return '{0}-{1}'.format(self.ref_code)                  
=======
from django.db import models
from django.contrib.auth import get_user_model
from myshopping.models import Product

# Get the user model
User = get_user_model()


# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.quantity} of {self.item.product_name}'

    def get_total(self):
        total = self.item.product_price * self.quantity
        floattotal = float("{0:.2f}".format(total))
        return floattotal

# Order Model
class Order(models.Model):
    orderitems  = models.ManyToManyField(Cart)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
<<<<<<< HEAD
        return self.user
>>>>>>> TestBranch3
=======
        return self.user.username


    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += order_item.get_total()
        
        return total
>>>>>>> TestBranch3
