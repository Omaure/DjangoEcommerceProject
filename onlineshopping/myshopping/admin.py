from django.contrib import admin

# Register your models here.
from .models import Product, Category, SubCategory, Brand

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Brand)
