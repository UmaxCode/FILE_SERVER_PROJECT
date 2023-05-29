from django.urls import path

from .views import (
    index,
    homepage_view,
    Document_View,
)


urlpatterns = [
    path('lizzy_server/', index, name='index'),
    path('lizzy_server/home/', homepage_view, name='home'),
    path('lizzy_server/home/<int:pk>/', Document_View.as_view(), name="details"),
]