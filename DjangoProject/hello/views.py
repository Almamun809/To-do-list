from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

def myView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'hello.html', {'all_items': all_todo_items})

def addTodo(request):
    c = request.POST['content']
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/hello/')

def deleteTodo(request, hello_id):
    item_to_delete = TodoItem.objects.get(id=hello_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/hello/')

def Home(request):
    return HttpResponse("This is a Todo List website. In Order to create a task list please change the directory '/hello' in the URL")

