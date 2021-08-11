from django.shortcuts import render, HttpResponse
from .models import ToDo

def homework(request):
    return HttpResponse ("Это мой первый проект Django")

def homepage(request):
    return render(request, "index.html")

def work(request):
    todo_list = ToDo.objects.all()
    return render(request, "work.html" {"todo_list": todo_list} )    
