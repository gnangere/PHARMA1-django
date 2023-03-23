from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth 
from django.contrib.auth.decorators import login_required

# verification send email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username=email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password )
            user.phone_number = phone_number
            user.save()
            # user activation
           
            messages.success(request, 'Registration Successful.')
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form':form,
    }

    return render(request,'accounts/register.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')

    return render(request,'accounts/login.html')
@login_required(login_url= 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are loggout out')
    return redirect('login')

def activate(request):
    return

def delete_user(request, user_id):
    user = get_object_or_404(Account, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request,'User deleted successfully.')
        return redirect('register')
    return render(request, 'accounts/delete_user.html', {'user':user})