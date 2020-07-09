from django.urls import path, include

from posts.api import *


app_name = 'api'
urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
]
