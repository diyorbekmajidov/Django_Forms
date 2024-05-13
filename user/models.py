from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    status = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=120, choices=status, default="regular")
    description =  models.TextField("Description", max_length=600, default='', blank=True)

    def __str__(self):
        return self.username

