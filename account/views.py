from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse

from django.views.generic.edit import CreateView
from .forms import (
    SignUpForm,
    LogInForm
)

from django.http import HttpResponse

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signUp_view(request):
    
    if request.method == "POST":
        
        form = SignUpForm(request.POST)

        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            con_password = form.cleaned_data.get('con_password')
            username = email[0]

            if password == con_password:  
              user = User.objects.create_user(username=username,email=email, password=password)
              user.save()
              return redirect('login')
        else:
            return render(request, 'account/signup.html', {
            'form': form
        })
            
    else:
        form = SignUpForm()
        return render(request, 'account/signup.html', {
            'form': form
        })


def login_view(request):
    
    if request.method == "POST":
        
        form = LogInForm(request.POST)

        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = email[0:3]

            user = authenticate(request, username=username, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'account/login.html', {
                'form':form,
                'message': 'Wrong email and password combination'
                })  
            

        else:
            return render(request, 'account/login.html', {
            'form':form
        })  
    
   
    form = LogInForm()
    return render(request, 'account/login.html', {
            'form':form
    })

