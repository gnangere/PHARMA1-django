from django import forms
from .models import Category, Shelf

class add_categoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['category_name','description']

    def __init__(self, *args, **kwargs):
        super(add_categoryForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs['placeholder'] = 'Enter category name'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter description'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
   
    