from django.db import models

class Account(models.Model):
    # blank = True # Boş değer olabilir.
    # null = True # Bir değer içermeyebilir.
    # unique = True # Aynı değer birden fazla yazılamaz.
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.username}"

# One to One:
class Profile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    profile_pic = models.ImageField(upload_to="profile_pics/",null=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.account} - {self.first_name} {self.last_name}"

'''
on_delete properties:
    # CASCADE -> if primary deleted, delete foreing too.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value')
    # DO_NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary.
'''

# Many to One: ForeignKey()
class Address(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.account} {self.name} {self.country}"

# Many to Many:
class Product(models.Model):
    account = models.ManyToManyField(Account) # Dont Use: on_delete
    brand = models.CharField(max_length=50)
    product = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.brand} {self.product}"










