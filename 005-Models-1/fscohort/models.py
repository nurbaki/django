from atexit import register
import email
from re import M
from tokenize import Number
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    number = models.IntegerField()
    about = models.TextField()
    register_date = models.DateField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.number} - {self.first_name}"

    class Meta:
        ordering = ["number"]
