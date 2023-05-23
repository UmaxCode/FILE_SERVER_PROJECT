from django.urls import path

from .views import (
    index,
    homepage_view
)


urlpatterns = [
    path('lizzy_server/', index, name='index'),
    path('lizzy_server/home', homepage_view, name='home')

]