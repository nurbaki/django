from django.db import models

class Student(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True, null=True)
    path = models.TextField(max_length=50, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    register_date = models.DateField(auto_now_add=True, null=True)
    last_update_date = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True, null=True)

    class Meta:
        ordering = ("first_name",)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"