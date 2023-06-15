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
from django.contrib import messages


from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .token import account_activation_token
from file_server_project.thread import EmailThread

# Create your views here.

def activate(request,uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Email verified . Now you can login.")
        return redirect("login")
    else:
        messages.error(request, "Activation link is invalid")

    return redirect("home")

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account"
    message =render_to_string("account/activate_account.html", {
        "user": user.username,
        "domain": get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        "token": account_activation_token.make_token(user),
        'protocol':'https' if request.is_secure() else "http"
    }
    )

    email = EmailMessage(mail_subject, message, to=[to_email])
    if EmailThread(email).start():
        messages.success(request, f"Dear {user}, please an activation link has be sent to your mail {to_email}.")
    else:
        messages.error(request, f"Problem sending email to {to_email}, check if you typed it correctly.")
    

def signUp_view(request):
    
    if request.method == "POST":
        
        form = SignUpForm(request.POST)

        if form.is_valid():
            
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            con_password = form.cleaned_data.get('con_password')
            username = form.cleaned_data.get('username')

            if password == con_password:  
              user = User.objects.create_user(username=username,email=email, password=password)
              user.is_active = False
              user.save()
              activateEmail(request, user, form.cleaned_data.get("email"))
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
            try:
                username = User.objects.get(email=email).username
            except:
                username = None
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

