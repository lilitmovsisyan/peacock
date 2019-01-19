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

def home(request):
    doc_title = "home"
    # retrieve all Entry objects from database (in reverse date order)
    entries_list = [e for e in Entry.objects.all().order_by('-date_published')] 
    # pass the first 10 entries for rendering in the home template
    return render(request, 'blog/home.html', {'doc_title': doc_title, 'entries_list': entries_list[:10]})

def index(request):
    doc_title = "index"
    # retrieve all Entry objects from database (in reverse date order)
    entries_list = [e for e in Entry.objects.all().order_by('-date_published')]
    # group entries_list into rows of 3 (row=sublist)
    rows = [entries_list[n:n+3] for n in range(0, len(entries_list), 3)]
    return render(request, 'blog/index.html', {'doc_title': doc_title, 'rows': rows})


"""this is still a GET request, but we need to tell it some info in an automated way.....
and the actual hyperlink in the index.html page needs to be malleable....
NB check urlpattern, too, as i work on this. 
"""
def project(request, project_title):
    #doc_title =  request #??????????need something else here and below
    #return render(request, 'blog/project.html', {'doc_title': "TEST", 'title': "TESTING"})
    return HttpResponse("TESTING")
    #return render(request, 'blog/project.html', {'doc_title': "TEST", 'title':slug})

