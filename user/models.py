from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
import os

class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("User", self.username, instance)
        return None
    
    status = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=120, choices=status, default="regular")
    description =  models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='default/5.jpeg', upload_to=image_upload_to)

    def __str__(self):
        return self.username
    


