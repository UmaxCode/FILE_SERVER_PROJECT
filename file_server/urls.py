from django.urls import path

from .views import (
    index,
    homepage_view,
    details_view,
    download_document,
)

urlpatterns = [
    path('lizzy_server/', index, name='index'),
    path('lizzy_server/home/', homepage_view, name='home'),
    path('lizzy_server/home/document/<int:pk>/',details_view, name="details"),
    path("lizzy_server/home/document/<int:pk>/download_document/", download_document, name="download_document")
]