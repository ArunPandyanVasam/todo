from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def addTask(request): #function always takes a request
    return HttpResponse('AddTask')