from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TodoItem
# Create your views here.
class TodoListView(ListView):
    model = TodoItem

class TodoDetailView(DetailView):
    model = TodoItem

class TodoCreate(CreateView):
    model = TodoItem
    fields = ['title', 'description']
    template_name = 'app/createTodo.html'
    success_url = reverse_lazy('todo:items')

class TodoUpdateView(UpdateView):
    model = TodoItem
    template_name = 'app/update.html'
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('todo:details', kwargs={'pk': self.object.id})

class TodoDeleteView(DeleteView):
    model = TodoItem
    template_name = 'app/delete.html'
    success_url = reverse_lazy('todo:items')