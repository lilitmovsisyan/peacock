from django.shortcuts import render
from django.http import HttpResponse
from .models import Entry, Tag

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
    # group entries_list into rows of 3 (row=sublist) for grid layout:
    # rows = [entries_list[n:n+3] for n in range(0, len(entries_list), 3)]
    return render(request, 'blog/index.html', {'doc_title': doc_title, 'entries': entries_list})

def bio(request):
    doc_title = "bio"
    return render(request, 'blog/bio.html', {'doc_title': doc_title})

# project page:
def project(request, project_id, project_title):
    #return render(request, 'blog/project.html', {'doc_title': "TEST", 'title': "TESTING"})
    #return HttpResponse("TESTING")
    entry = Entry.objects.all().get(id=project_id)
    doc_title = entry.title
    return render(request, 'blog/project.html', {'doc_title': doc_title, 'entry': entry})

def taglist(request):
    doc_title = "tags"
    tags_list = [t for t in Tag.objects.all().order_by('name')]
    return render(request, 'blog/taglist.html', {'doc_title': doc_title, 'tags_list': tags_list})

def tagpage(request, tag_name):
    doc_title = "#" + tag_name
    tag = Tag.objects.get(name=tag_name)
    matching_entries = [e for e in tag.entry_set.all()]
    return render(request, 'blog/tagpage.html', {'doc_title': doc_title, 'matching_entries': matching_entries})


"""NOTES:
entry = Entry.objects.all().filter(id=1) --> the .filter() function returns a QuerySet! This is not always what we want!
entry = Entry.objects.all().get(id=1) --> in contrast, the .get() function returns a single object! We can then call things like the various field attributes on this object (e.g. entry.title to retrieve the title)
"""