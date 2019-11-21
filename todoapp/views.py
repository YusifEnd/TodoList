from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {"todos": todos})


def detail(request, pk):
    todos = get_object_or_404(Todo, pk=pk)
    return render(request, 'detail.html', {"todos": todos})


def addTodo(request):
    if request.method == "GET":
        return redirect("/")
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        due_date = request.POST.get('due_date')
        new_todo = Todo(title=title, content=content, due_date=due_date, completed=False)

        new_todo.save()
        return redirect("/")


def update(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect("/")


def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("/")



