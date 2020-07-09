from django.urls import path

from posts.api import *


app_name = 'api'
urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
]
