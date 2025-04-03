from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.age is not None and self.age < 15:
            self.can_be_contacted = False
            self.can_data_be_shared = False
            raise ValueError("L'utilisateur doit avoir au moins 15 ans.")
        super().save(*args, **kwargs)
