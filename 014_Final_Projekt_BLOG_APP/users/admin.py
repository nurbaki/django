from django.contrib import admin
from .models import Profile, Category, Post, Comment, Like, PostView

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)


