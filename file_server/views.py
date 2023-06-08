from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import DetailView
from pathlib import Path
from django.core.mail import EmailMessage
from .models import Document

# Create your views here.

def index(request):
    
    return render(request, 'file_server/index.html')


@login_required
def homepage_view(request):

    documents = Document.objects.all()
    search_text = ""
    
    if request.method == "POST":
        search_text = request.POST["search"]

        if len(search_text):
            query_result = Document.objects.filter(Q(title__icontains=f"{search_text}") | Q(description__icontains=f"{search_text}"))
            documents = query_result


    context = {
        "user_profile":request.user,
        "documents": documents,
        'search_text': search_text
        }
    return render(request, 'file_server/feed_page.html', context)

class Document_View(DetailView):

    model = Document

    template_name = "file_server/details.html"

    context_object_name = 'document'



def details_view(request, pk):

    if request.method == "POST":
        document = Document.objects.get(pk=pk)

        email = request.POST["email"]

        title = document.title
        description = document.description
        file = document.file

        email_send = EmailMessage(title, description,'settings.EMAIL_HOST_USER', [email])

        email_send.attach_file(file.path)
        email_send.send()

        return redirect("details", pk=pk)
        

    document = Document.objects.get(pk=pk)

    context = {
        "document": document
    }

    return render(request, "file_server/details.html", context)


def download_document(request, pk):
    document = Document.objects.get(pk=pk)
    file_path = document.file.path

    with open(file_path, 'rb') as file:
        
        data = file.read()

        extension = getFileExtension(file_path)

        if extension == '.pdf':
            response = HttpResponse(data, content_type='application/pdf')
        elif extension == '.mp4':
            response = HttpResponse(data, content_type='video/mp4')
        elif extension == '.mp3':
            response = HttpResponse(data, content_type='audio/mpeg')
        elif extension == ".jpg":
            response = HttpResponse(data, content_type='image/jpeg')
        else:
            response = HttpResponse(data, content_type='application/octet-stream')
        response['Content_Disposition']='attachment;'

    return response

def getFileExtension(file_path):
    path = Path(file_path)
    return path.suffix
