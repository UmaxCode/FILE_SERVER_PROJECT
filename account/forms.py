from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.models import User


class SignUpForm(forms.Form):

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'placeholder': 'username'
        })
      
    )
    
    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'email'
        })
      
    )

    password = forms.CharField(
        label="Password", 
    widget=forms.PasswordInput(attrs={
        'placeholder': 'password'
    })
    
    )

    con_password = forms.CharField(
        label="Confirm Password", 
    widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm password'
    })
    )



class LogInForm(forms.Form):
    
    email = forms.CharField(
        label="Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'email'
        })
          )

    password = forms.CharField(
        label="Password", 
    widget=forms.PasswordInput(attrs={
        'placeholder':'password'
    })
    )
