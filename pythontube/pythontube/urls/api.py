from django.urls import path, include

from posts.api import *


app_name = 'api'
urlpatterns = [
    path('posts/', include([
        path('', PostListAPIView.as_view(), name="list"),
        path('<slug:slug>/comments', PostCommentListAPIView.as_view(), name="comments"),
        ])
        )
    ]
