from django.urls import path

from .views import (
    signUp_view,
    login_view
)

urlpatterns = [
    path('login/', login_view, name='cus_login'),
    path('signup/', signUp_view, name='signup')
]