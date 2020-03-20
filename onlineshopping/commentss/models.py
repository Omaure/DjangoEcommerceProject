from django.db import models
from myshopping.models import Product
# Create your models here.
class Comment(models.Model):
    product=models.ForeignKey(Product,related_name='comments',on_delete=models.CASCADE)
    user=models.CharField(max_length=250)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    approved=models.BooleanField(default=False)
    def approved(self):
        self.approved=True
        self.save()
    def __str__(self):
        return self.user    


