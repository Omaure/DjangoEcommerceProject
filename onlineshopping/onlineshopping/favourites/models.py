from django.db import models
from django.contrib.auth import get_user_model
from myshopping.models import Product


# Get the user model
User = get_user_model()

# Create your models here.

class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favitem = models.ForeignKey(Product, on_delete=models.CASCADE)

