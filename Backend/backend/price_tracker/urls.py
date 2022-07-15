from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from price_tracker.api import ProductsList, ProductDetail,check_products


urlpatterns = [
    path('<int:pk>', ProductDetail.as_view()),
    path('', ProductsList.as_view()),
    path('check_products',check_products),
]

urlpatterns = format_suffix_patterns(urlpatterns)