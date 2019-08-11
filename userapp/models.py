from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models

# Create your models here.

class UserMangaer(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, middle_name=None, password=None,is_active=False):
        user = self.model(username=username, email=self.normalize_email(email), first_name=first_name, last_name=last_name, middle_name=middle_name,is_active=is_active)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email,  first_name, last_name, password=None ,middle_name=None):
        user = self.create_user(username, email, first_name, last_name, password=password ,middle_name=middle_name,is_active=True)
        user.is_superuser = True
        user.is_staff = True
    
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True,max_length=255,unique=True)
    email = models.EmailField(db_index=True,unique=True,blank=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=30,blank=False)
    middle_name = models.CharField(max_length=30,null=True,blank=True)
    last_name = models.CharField(max_length=30,blank=False)
    
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email','first_name','last_name']

    objects = UserMangaer()

    def __str__(self):
        return self.username