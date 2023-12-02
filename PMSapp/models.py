from django.db import models
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class MemberManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class Member(AbstractBaseUser, PermissionsMixin):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    passwordconfirm = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='pmsapp_member_user_permissions',
        blank=True,
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='pmsapp_member_user_groups',
        blank=True,
    )

    objects = MemberManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'fname', 'lname']

    def __str__(self):
        return self.username

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