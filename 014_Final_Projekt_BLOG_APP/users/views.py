from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User

from users.models import Post, Profile
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

# class ProfileCreate(CreateView):
#     model = Profile
#     form_class = UserProfileForm
#     template_name = "users/profile_add.html"
#     success_url = reverse_lazy("profile")

# class ProfileUpdate(UpdateView):
#     model = User
#     form_class = UserForm
#     template_name = "users/profile_update.html"
#     success_url = reverse_lazy("profile")
#     pk = 'id'

def profileUpdate(request):
    user = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user)

    form_profile = UserProfileForm(instance=user_profile)

    if request.method == 'POST':

        form_profile = UserProfileForm(request.POST, request.FILES, instance= user_profile)

        if form_profile.is_valid():
            form_profile.save()
            return redirect('profile')


    context = {
        'form_profile' : form_profile
    }
    return render(request, 'users/profile_update.html', context)



def profileDetail(request):
    user = User.objects.get(username = request.user)
    user_profile = Profile.objects.get(user = user)
    context = {
        'user_profile' : user_profile
    }
    return render(request, 'users/profile.html', context)
 
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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "users/post_create.html"
    success_url = reverse_lazy("post_list")

    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    pk = 'id'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "users/post_update.html"
    success_url = reverse_lazy("post_list")
    pk = 'id'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'users/post_delete.html'
    success_url = reverse_lazy("post_list")
    pk = 'id'
