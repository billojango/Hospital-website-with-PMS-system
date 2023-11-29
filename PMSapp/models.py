from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password


# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    passwordconfirm = models.CharField(max_length=20)

    def __str__(self):
        return self.fname


class Patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    date = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    message = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name



class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Payment(models.Model):
    phone = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.phone} - Ksh{self.amount}"