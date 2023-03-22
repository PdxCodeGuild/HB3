from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo
from .forms import RegisterTodo, TodoForm
import random
# Create your views here.
# def index(request):
#     return render(request, "index.html", {'name': 'Jane'})

# def index(request):
#     return render(request, "index.html", {'temperature': random.randint(50, 100)})
# def index(request):
#     fruits = {'fruits': ['apples', 'bananas', 'pears']}
#     return render(request, "index.html", fruits)

# def detail(request, todo_id):
#     todo_item = Todo.objects.all()
#     print(todo_id)
#     context = {todo_item: todo_item}
#     return render(request, 'details.html', context)

# def formSubmit(request):
#     user_input = request.POST.get('our_text')
#     print(user_input)
#     return HttpResponse("done")

# import json
# def postdata(request):
#     data = json.loads(request.body)
#     sent_data = json.dump('some.json')
#     print(data)

# def fruits(request):
#     fruits = ['apples', 'bananas', 'plums']
#     html = '<ul>'
#     for fruit in fruits:
#         html += '<li>' + fruit + '</li>'
#     html += '</ul>'
#     return HttpResponse(html)

# def todo_items(request):
#     todo_items = Todo.objects.all()
#     context = {'todo_items': todo_items}
#     return render(request, 'index.html', context)

# def json_response(request):
#     data = {'foo': 'bar', 'hello': 'world'}
#     return JsonResponse(data)

# def url_redirect(request):
#     return HttpResponseRedirect("/fruits/")

# def index(request):
#     return render(request, 'index.html')

def show_todo(request):
    title = request.POST['title']
    todo = Todo(title=title)
    todo.save()
    return render(request, 'index.html')

def save_todo(request):
    if request.method == 'POST':
        form = RegisterTodo(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            print(title)
            todo_item = Todo(title=title)
            todo_item.save()
            form = RegisterTodo()
    else:
        form = RegisterTodo()
    return render(request, 'index.html', {'form':form})

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()
    else:
        form = TodoForm()
    return render(request, 'index.html', {'form': form})