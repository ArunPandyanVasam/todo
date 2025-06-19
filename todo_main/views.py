from django.shortcuts import render
from todoApp.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False)
    #print(tasks)
    context = {
        'tasks': tasks # orange task123 can also we can name it
    }
    return render(request, 'home.html', context)