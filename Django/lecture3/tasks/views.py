from django.shortcuts import render
from .forms import NewTask
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] =[]
        
    return render(request,'tasks/index.html',{
        "tasks":request.session["tasks"]
    })
    
def add(request):
    if request.method =='POST':
        form = NewTask(request.POST)
        if form.is_valid():
            task =form.cleaned_data["task"]
            request.session["tasks"]+=[task]
            return HttpResponseRedirect(reverse("tasks"))
        else:
            return render(request,'tasks/add.html',{
                "form":form
            })
    return render(request,'tasks/add.html',{
        "form":NewTask()
    })