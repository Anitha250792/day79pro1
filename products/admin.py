

# Register your models here.
from django.contrib import admin

from .models import Product
 
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'price', 'in_stock')  # Display these in admin list view

    list_filter = ('in_stock',)

    search_fields = ('name', 'description')

 