from django.contrib import admin
from .models import Category, Shelf

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('category_name',)}
    list_display = ('category_name', 'slug','description')
class ShelfAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('shelf_name',)}
    list_display = ('shelf_name', 'slug')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Shelf, ShelfAdmin)

