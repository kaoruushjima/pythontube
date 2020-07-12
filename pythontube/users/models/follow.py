from django.db import models


class Follow(models.Model):
    follower = models.ForeignKey(
        "User",
        related_name="+",
        on_delete=models.CASCADE
    )
    followee = models.ForeignKey(
        "User",
        related_name="+",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
