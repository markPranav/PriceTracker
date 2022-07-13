from django.db import models
from users.models import User


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null= False)
    url = models.URLField(blank=False, null=False, unique=True)

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    availability = models.BooleanField(blank=False, null=False)
    actual_price = models.FloatField(blank=True, null=True)
    sell_price = models.FloatField(blank=False, null=False)

class Tracker(models.Model):
    price_hist = models.ForeignKey(PriceHistory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target_price = models.FloatField(blank=False, null=False)
    send_email = models.BooleanField()
    send_telegram = models.BooleanField()
    send_sms = models.BooleanField()
    send_discord = models.BooleanField()