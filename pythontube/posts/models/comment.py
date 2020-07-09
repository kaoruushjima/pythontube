from django.db import models

from users.models import User


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # user.comment_set , post.comment_set으로 불러 올 수 있게 된다
    def __str__(self):
        return self.content
