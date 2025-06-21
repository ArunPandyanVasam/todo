from django.shortcuts import render
from todoApp.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') # tasks = Task.objects.filter(is_completed=False),     #print(tasks)
    completed_tasks = Task.objects.filter(is_completed=True) # print(completed_tasks)

    context = {
        'tasks': tasks, # orange task123 can also we can name it as our wish
        'completed_tasks': completed_tasks
    }
    return render(request, 'home.html', context)