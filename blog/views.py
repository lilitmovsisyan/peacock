from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("So what's the issue?")

    return render(request, 'blog/home.html', {})
