from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display =('product_name','slug','price','quantity', 'category', 'modified_date','is_available','images')
    prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Product,ProductAdmin)