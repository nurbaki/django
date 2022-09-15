from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('home')

def register(request):
    # form = UserForm()
    form = UserForm(request.POST or None)

    # if request.method == 'POST':
    #     # pass in post data when instantiate the form.
    #     form = UserForm(request.POST, request.FILES)
    #     # if the form is ok with the info filled:
    if form.is_valid():
        user = form.save()
        
        # want user to login right after registered, import login
        login(request, user)
        messages.success(request, 'Registered Successfully!!')
        # want to redirect to home page, import redirect
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, "users/register.html", context)




def user_login(request):
    form = AuthenticationForm(request, request.POST or None)

    if form.is_valid():
        user = form.get_user()
        if user:
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('home')

    context = {
        'form': form
    }
    
    return render(request, 'users/user_login.html', context)

