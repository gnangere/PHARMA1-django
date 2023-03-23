from django.shortcuts import render
from .models import Category
from .forms import add_categoryForm
from django.contrib import messages 

def add_category(request):
    if request.method == "POST":
            form = add_categoryForm(request.POST)
            if form.is_valid:
                form.save()
                messages.success(request, 'Category Successfully created')
    else :
          form = add_categoryForm()
                  
    context ={
        'form': form
    }

    return render(request,'category/add_category.html',context)