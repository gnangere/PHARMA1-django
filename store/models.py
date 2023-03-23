from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500,blank=True)
    quantity = models.IntegerField()
    FORM_CHOICES = (
        ("FL", "FLACON"),
        ("BT", "BOITE"),
        ("TB", "TUBE"),
        ("CT", "CARTON"),

    )
    form = models.CharField(max_length=20, choices=FORM_CHOICES, default="BOITE")
    stock_min = models.IntegerField(default=0)
    stock_max = models.IntegerField(default=0)
    price = models.IntegerField()
    is_available = models.BooleanField(default= True)
    category = models.ForeignKey(Category, on_delete =models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    in_amo = models.BooleanField(default= False)
    images = models.ImageField(upload_to='photos/products')

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name