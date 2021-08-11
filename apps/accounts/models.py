from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    last_active = models.DateTimeField(
        'last active',
        blank=True,
        null=True
    )
