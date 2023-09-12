# from django.contrib.auth.models import AbstractUser, User
# from django.db import models
# from django.db.models import Model, CASCADE, CharField, ImageField, EmailField, DateField, TextField,DateTimeField
#
#
# class UserProfile(AbstractUser):
#     name = CharField(max_length=100)
#     password = CharField(max_length=8)
#     # email = EmailField(unique=True)
#     # phone = CharField(max_length=100)
#     # date_of_birth = DateField(blank=True, null=True)
#     # image = ImageField(upload_to='profile_images', blank=True, null=True)
#     # bio = TextField(max_length=1000)
#     created_at = DateTimeField(auto_now_add=True)
#     updated_at = DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         app_label = 'user'
#         ordering = ['-created_at']

from django.contrib.auth.models import AbstractUser
from django.db.models import DateTimeField, CharField


class User(AbstractUser):
    place = CharField(max_length=64, null=True, blank=True)
    address = CharField(max_length=128, null=True, blank=True)
