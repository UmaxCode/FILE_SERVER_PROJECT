from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return render(request, 'file_server/index.html')

def homepage_view(request):



    context = {
        "user_profile":request.user,
        "documents": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5 ,6, 3, 4, 5 ,6 ,6, 6, 7, 7, 7, 7 ,7, 7, 7 ,7, 7]
        }
    return render(request, 'file_server/feed_page.html', context)