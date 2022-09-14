from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'user_example/index.html')


def special(request):
    return render(request, "user_example/special.html")

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)
