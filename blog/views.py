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
    # retrieve all Entry objects from database
    entries_list = [e for e in Entry.objects.all()] 
    # pass the first 10 entries for rendering in the home template
    return render(request, 'blog/home.html', {'entries_list': entries_list[:10]})
