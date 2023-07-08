from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.



class CustomUser(AbstractUser):
    username=None
    email=models.EmailField(max_length=254,unique=True)
    bio=models.TextField()
    address=models.CharField(max_length=50)

    objects=UserManager()

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=[]