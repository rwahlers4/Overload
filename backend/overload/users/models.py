from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(blank=True, max_length=64,unique=True)
    username = models.CharField(max_length=48, default="USERNAME", unique=True)
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    

