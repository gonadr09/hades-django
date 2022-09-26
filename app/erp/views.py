from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def firstview(request):
    #return HttpResponse("hola mundo")
    return render(request, "index.html")