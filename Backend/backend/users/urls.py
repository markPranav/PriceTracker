from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users.api import UsersList, UserDetail, create_user

urlpatterns = [
    path('', UserDetail.as_view()),
    path('create/', create_user),
    path('admin', UsersList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)