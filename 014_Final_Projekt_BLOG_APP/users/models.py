from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='profile_pic', blank=True)
    # image = models.ImageField(upload_to='profile_pic', blank=True, default="avatar.png")


    def __str__(self):
        return self.user.username

    
class Category(models.Model):
    CATEGORY =(
        ("1", "Frontend"),
        ("2", "Backend"),
        ("3", "Full-Stack"),
    )
    name = models.CharField(max_length=50, choices=CATEGORY)


class Post(models.Model):
    Status =(
        ("1", "Draft"),
        ("2", "Published"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_image', blank=True)
    publish_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=Status)
    slug = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateField(auto_now_add=True)
    content = models.TextField()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    view_number = models.IntegerField(blank=True, null=True)