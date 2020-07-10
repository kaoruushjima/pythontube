from django.db import models

from posts.models import Post


class Like(models.Model):

    user = models.ForeignKey("User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # user => user.like_set.all() # like model Queryset # => Post model queryset
    # post => user.like_set.all() # like model Queryset # => User model queryset
