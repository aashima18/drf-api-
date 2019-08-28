from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(max_length=254)
    username = models.CharField(unique=True,max_length=254,)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
   
    
class Item(models.Model):
    title = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=500, null=True)
    user_s = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    def __str__(self):
        
        return self.title
    
    