# from __future__ import unicode_literals
from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
<<<<<<< HEAD

=======
>>>>>>> TestBranch4

=======
import datetime
from datetime import date
>>>>>>> TestBranch1
# Create your models here.
# -*- coding: utf-8 -*-


class Category(models.Model):
    cat_name = models.CharField(max_length=120)
<<<<<<< HEAD
    cat_id = models.IntegerField()
    cat_description = models.CharField(max_length=300)
=======
    cat_id = models.IntegerField(primary_key=True)
    cat_description=models.CharField(max_length=400)
    cat_image=models.ImageField(upload_to='gallery',default='default.jpg')
>>>>>>> TestBranch4

    def __str__(self):
        return self.cat_name

<<<<<<< HEAD

class SubCategory(models.Model):
    subcat_name = models.CharField(max_length=120)
    subcat_id = models.IntegerField()
    subcat_description = models.CharField(max_length=300)

    def __str__(self):
        return self.subcat_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=120)
    brand_id = models.IntegerField()
    brand_cat_id = models.IntegerField()

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    product_id = models.IntegerField()
    product_subcat_id = models.IntegerField()
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
<<<<<<< HEAD
    image1 = models.ImageField(upload_to='gallery')

=======
    image1 = models.ImageField(upload_to='products/', blank=True)
    slug = models.SlugField()
    
>>>>>>> TestBranch3
    def __str__(self):
        return self.product_name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    DOB = models.DateTimeField(default=datetime.date.today, blank=True)
    location = models.CharField(max_length=200, default="None")

    def __str__(self):
        return self.user.username
=======
class SubCategory(models.Model):
    subcat_name  = models.CharField(max_length=120)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat_id = models.IntegerField(primary_key=True)
    subcat_description=models.CharField(max_length=300)
    subcat_image=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.subcat_name 
    def get_absolute_url(self):
        return reverse("myshopping:product", kwargs={
            'slug': self.slug
        })    

class Brand(models.Model):
    name = models.CharField(max_length=120)
    brand=models.IntegerField(primary_key=True)
    subcat_id=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand_img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=120)
    product_id = models.IntegerField(primary_key=True)
    product_brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    product_price=models.IntegerField()
    image1=models.ImageField(upload_to='gallery')
    image2=models.ImageField(upload_to='gallery')
    image3=models.ImageField(upload_to='gallery')
    

    def __str__(self):
        return self.product_name
        
>>>>>>> TestBranch4
