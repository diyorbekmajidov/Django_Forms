from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
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
    

class ManagerCustomUser(BaseUserManager):
    def create_user(self, password, email, **extra_feild):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_feild)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(password, email, **extra_fields)
    
    
class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email

