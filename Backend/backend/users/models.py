from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=70, blank=True)
    discord_id = models.CharField(max_length=70, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    password = models.CharField(max_length=150, blank=True)
    