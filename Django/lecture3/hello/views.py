from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'hello/index.html')
def brian(request):
    return HttpResponse("hello- brian-whats up!")
def devid(request):
    return HttpResponse("hello devid whats upppp")

def greet(request,name):
    return render(request,'hello/greet.html',{
        'name': name.capitalize()
    })