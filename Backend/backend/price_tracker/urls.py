from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from price_tracker.api import ProductsList, ProductDetail

urlpatterns = [
    path('<int:pk>', ProductDetail.as_view()),
    path('', ProductsList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)