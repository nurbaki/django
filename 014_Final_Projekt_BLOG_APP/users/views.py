from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages

from users.models import Post
from .forms import UserForm, UserProfileForm, PostForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
    )


def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('home')

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        # uploaded files coming from request.FILES
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            # form_user.save()
            # form_profile.save()

            # we need to define user for profile before save
            # how to get the user?
            user = form_user.save()
            profile = form_profile.save(commit=False)
            # get the profile info without saving to db

            profile.user = user
            # now we know the user

            profile.save()
            login(request, user)
            messages.success(request, 'Registered Successfully!!')

            return redirect('home')


    context = {
        'form_user' : form_user,
        'form_profile' : form_profile
    }
    return render(request, 'users/register.html', context)


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




# class HomeView(TemplateView):
#     template_name = "users/home.html"
    
#     def get_context_data(self,  **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post'] = Post.objects.all()
#         return context

class PostListView(ListView):
    model = Post
    template_name = "users/post_list.html"
    
    # queryset = Student.objects.filter(number=123)

    # def get_queryset(self):
    #     queryset = super().get_queryset(self)
    #     return queryset

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "users/post_create.html"
    success_url = reverse_lazy("post_list")


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'id'


# class StudentUpdateView(UpdateView):
#     model = Student
#     form_class = StudentForm
#     template_name = "fscohort/student_update.html"
#     success_url = reverse_lazy("list")


# class StudentDeleteView(DeleteView):
#     model = Student
#     template_name = 'fscohort/student_delete.html'
#     success_url = reverse_lazy("list")
