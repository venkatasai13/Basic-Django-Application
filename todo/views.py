from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'todo/list.html'
    context_object_name = 'todos'

class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'description', 'is_active']
    template_name = 'todo/create.html'
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'description', 'is_active']
    template_name = 'todo/update.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo_list')
