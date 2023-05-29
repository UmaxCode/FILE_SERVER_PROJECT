from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView

from django.core.files.storage import FileSystemStorage

from .models import Document
# Create your views here.

def index(request):
    
    return render(request, 'file_server/index.html')


@login_required
def homepage_view(request):

    documents = Document.objects.all()
    
    context = {
        "user_profile":request.user,
        "documents": documents
        }
    return render(request, 'file_server/feed_page.html', context)

class Document_View(DetailView):

    model = Document

    template_name = "file_server/details.html"

    context_object_name = 'document'


    

