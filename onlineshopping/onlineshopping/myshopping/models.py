from __future__ import unicode_literals
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-


class Category(models.Model):
    cat_name = models.CharField(max_length=120)
    cat_id = models.IntegerField(primary_key=True)
    cat_description=models.CharField(max_length=400)
    cat_image=models.ImageField(upload_to='gallery',default='default.jpg')

    def __str__(self):
        return self.cat_name

class SubCategory(models.Model):
    subcat_name  = models.CharField(max_length=120)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat_id = models.IntegerField(primary_key=True)
    subcat_description=models.CharField(max_length=300)
    subcat_image=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.subcat_name 

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
