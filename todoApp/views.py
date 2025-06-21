from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task #from todoApp.models import Task

# Create your views here.
def addTask(request): #function always takes a request
    task = request.POST['task'] #print(request.POST['task'])  #print(request.POST)
    Task.objects.create(task=task) #left task is the variable and right task is field from Task model
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk) #left pk is actually the field name of the task model and right pk is the dynamic primary key we are passing. 
    task.is_completed = True # task is object from top line and is_completed is field from model
    task.save() # now save
    return redirect('home')#return HttpResponse(task) #return HttpResponse(pk)

def mark_as_undo(request, pk):
    task = get_object_or_404(Task, pk=pk) #left pk is actually the field name of the task model and right pk is the dynamic primary key we are passing. 
    task.is_completed = False # task is object from top line and is_completed is field from model
    task.save() # now save
    return redirect('home') # return HttpResponse(task) #return HttpResponse(pk)

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task #print(new_task)
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task
        }
        return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')