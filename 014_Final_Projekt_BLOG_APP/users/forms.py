from dataclasses import field
from pyexpat import model
from socket import fromshare
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ('potfolio', 'profile_pic')
        exclude = ('user',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        exclude = ('user', 'slug')