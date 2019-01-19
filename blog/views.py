from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry

# Create your views here.

"""
def home(request):
    #return HttpResponse("So what's the issue?")
    entry = Entry

    return render(request, 'blog/home.html', {'entry': entry})
"""

# blog post style home page, showing ten most recent posts as you scroll down the page:
def home(request):
    doc_title = "home"
    # retrieve all Entry objects from database (in reverse date order)
    entries_list = [e for e in Entry.objects.all().order_by('-date_published')] 
    # pass the first 10 entries for rendering in the home template
    return render(request, 'blog/home.html', {'doc_title': doc_title, 'entries_list': entries_list[:10]})

# grid layout home page, showing title of each project:
def index(request):
    doc_title = "index"
    # retrieve all Entry objects from database (in reverse date order)
    entries_list = [e for e in Entry.objects.all().order_by('-date_published')]
    # group entries_list into rows of 3 (row=sublist)
    rows = [entries_list[n:n+3] for n in range(0, len(entries_list), 3)]
    return render(request, 'blog/index.html', {'doc_title': doc_title, 'rows': rows})


# project page:
def project(request, project_title):
    #doc_title =  request #??????????need something else here and below
    #return render(request, 'blog/project.html', {'doc_title': "TEST", 'title': "TESTING"})
    return HttpResponse("TESTING")
    #return render(request, 'blog/project.html', {'doc_title': "TEST", 'title':slug})

