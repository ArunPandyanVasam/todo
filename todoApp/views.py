from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task #from todoApp.models import Task

# Create your views here.
def addTask(request): #function always takes a request
    task = request.POST['task'] #print(request.POST['task'])  #print(request.POST)
    Task.objects.create(task=task) #left task is the variable and right task is field from Task model
    return redirect('home')

def mark_as_done(request, pk):
    return HttpResponse(pk)