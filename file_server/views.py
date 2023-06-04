from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from django.views.generic import DetailView

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from .models import Document
# Create your views here.

def index(request):
    
    return render(request, 'file_server/index.html')


@login_required
def homepage_view(request):

    if request.method == "POST":
        search_text = request.POST["search"]

        return HttpResponse(f"The search text is {search_text}")

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



def details_view(request, pk):

    if request.method == "POST":
        document = Document.objects.get(pk=pk)

        email = request.POST["email"]

        title = document.title
        description = document.description
        file = document.file

        # send_mail(title, description, 'settings.EMAIL_HOST_USER', 
        # [email], fail_silently=False)

        email_send = EmailMessage(title, description,'settings.EMAIL_HOST_USER', [email])

        email_send.attach_file(file.path)
        email_send.send()

        return redirect("details", pk=pk)
        

    document = Document.objects.get(pk=pk)

    context = {
        "document": document
    }

    return render(request, "file_server/details.html", context)




    


    

