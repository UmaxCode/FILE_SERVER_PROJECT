from django.urls import path

from .views import (
    index,
    homepage_view,
    details_view,
)

urlpatterns = [
    path('lizzy_server/', index, name='index'),
    path('lizzy_server/home/', homepage_view, name='home'),
    path('lizzy_server/home/<int:pk>/',details_view, name="details"),
]