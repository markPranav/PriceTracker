from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from durin import views as durin_views
from .api import LoginView


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('refresh/', durin_views.RefreshView.as_view()),
    path('logout/', durin_views.LogoutView.as_view()),
    path('logoutall/', durin_views.LogoutAllView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)