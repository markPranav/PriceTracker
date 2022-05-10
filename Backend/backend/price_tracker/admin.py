from django.contrib import admin
from price_tracker.models import PriceHistory, Tracker

from price_tracker.models import Product

# Register your models here.
admin.site.register(Product)
admin.site.register(PriceHistory)
admin.site.register(Tracker)