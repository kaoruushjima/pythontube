# Django Model은 Meta => abstract=True (테이블X)라고 되어있지 않으면, 모델을 상속할 수 없다.
from django.contrib.auth.models import AbstractUser
from django.db import models

from .follow import Follow


class User(AbstractUser):

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    # 단일 모델에서의 M2M관계 => 대칭적 SYMMETRIC (FOLLOWER, FOLLOWEE)
    # Follow라는 행위에 대해서, Follower(주체) => Followee(객체)

    follower_set = models.ManyToManyField(
        "self",
        symmetrical=False,
        through=Follow,
        through_fields=("followee", "follower"),
        related_name="followee_set",
    )
