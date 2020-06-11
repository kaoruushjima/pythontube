from django.urls import path

from posts.views import *


app_name = 'posts'
urlpatterns = [
    path('new/', PostCreateFormView.as_view(), name="new"),
]
