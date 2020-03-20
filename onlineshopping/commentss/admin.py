from django.contrib import admin
from myshopping.models import Product
from .models import Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display=('user','approved')

admin.site.register(Comment,CommentAdmin)    