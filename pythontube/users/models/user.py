# Django Model은 Meta => abstract=True (테이블X)라고 되어있지 않으면, 모델을 상속할 수 없다.
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )
