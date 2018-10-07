from django.shortcuts import render
#from django.http import HttpResponse
from .models import Entry

# Create your views here.
def home(request):
    #return HttpResponse("So what's the issue?")
    entry = Entry

    return render(request, 'blog/home.html', {'entry': entry})
