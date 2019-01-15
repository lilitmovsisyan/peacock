from django.shortcuts import render
#from django.http import HttpResponse
from .models import Entry

# Create your views here.

"""
def home(request):
    #return HttpResponse("So what's the issue?")
    entry = Entry

    return render(request, 'blog/home.html', {'entry': entry})
"""

def home(request):
    doc_title = "home"
    # retrieve all Entry objects from database (in reverse date order)
    entries_list = [e for e in Entry.objects.all().order_by('-date_published')] 
    # pass the first 10 entries for rendering in the home template
    return render(request, 'blog/home.html', {'doc_title': doc_title, 'entries_list': entries_list[:10]})

def index(request):
    doc_title = "index"

    return render(request, 'blog/index.html', {'doc_title': doc_title})