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
