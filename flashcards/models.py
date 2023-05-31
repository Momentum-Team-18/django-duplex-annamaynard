from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length =30, blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    
    
# Create your models here.
