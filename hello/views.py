from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"hello/index.html")
 
def tirth(request):
     return HttpResponse("Hello Tirth.")

def janki(request):
    return HttpResponse("Hello Janki.")

def greet(request,name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })