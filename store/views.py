from django.shortcuts import render
from store.models import Product

def store(request):
    products= Product.objects.all().filter(is_available=True)
    context ={
        'products':products
    }
    return render(request,'store/store.html',context)


def product_detail(request):
    return render(request, 'store/product_detail.html')
