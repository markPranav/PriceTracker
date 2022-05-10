from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=70)
    discord_id = models.CharField(max_length=70)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=150)
    