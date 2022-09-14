from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# def home(request):
#     todos = Todo.objects.all()
#     form = TodoForm
#     context = {
#         "todos" : todos,
#         "form" : form
#     }
#     return render(request, "todo/home.html", context)


class TodoHome(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/home.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        kwargs["todos"] = Todo.objects.order_by('priority')
        return super().get_context_data(**kwargs)


# def todo_create(request):
#     form = TodoForm
    
#     if request.method == "POST":
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Todo created successfully")
#             return redirect("home")
    
#     context = {
#         "form" : form
#     }
    
#     return render(request, "todo/todo_add.html", context)

class TodoCreate(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_add.html"
    success_url = reverse_lazy("home")


# def todo_update(request, id):
#     todo = Todo.objects.get(id=id)
#     form = TodoForm(instance=todo)
    
#     if request.method == "POST":
#         form = TodoForm(request.POST, instance=todo)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Todo updated successfully")
#             return redirect("home")

#     context = {
#         "form" : form
#     }
    
#     return render(request, "todo/todo_update.html", context)


class TodoUpdate(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todo/todo_update.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "id"  # eger primary key ile islem yapacaksak buna da gerek yok



def todo_delete(request, id):
    
    todo = Todo.objects.get(id=id)
    
    if request.method == "POST":
        todo.delete()
        messages.success(request,"Todo deleted successfully")
        return redirect("home")
    
    context = {
        "todo": todo
    }
    
    return render(request, "todo/todo_delete.html", context)