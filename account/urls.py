from django.urls import path

from .views import (
    signUp_view,
    login_view,
    activate
)

urlpatterns = [
    path('login/', login_view, name='cus_login'),
    path('signup/', signUp_view, name='signup'),
    path("activate/<uidb64>/<token>", activate, name="activate")
]