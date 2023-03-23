from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=1000, blank=True)

    class Meta:
        verbose_name ='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.category_name
    def get_url(self):
        return reverse('products_by_category', args=[self.slug])
   
        

class Shelf(models.Model):
    shelf_name= models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:

        verbose_name ='shelf'
        verbose_name_plural='shelfs'
    def __str__(self):
        return self.shelf_name

