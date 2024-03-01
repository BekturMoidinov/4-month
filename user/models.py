from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


# class User(AbstractBaseUser):
#     first_name = models.CharField(max_length=50, blank=True)
#     last_name = models.CharField(max_length=50, blank=True)
#     email = models.EmailField(unique=True)
#     age = models.PositiveSmallIntegerField(null=True, blank=True)
#     avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
#     bio = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.first_name

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE,related_name='profile')
    age = models.PositiveIntegerField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class SMScode(models.Model): 
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,related_name='smscode')
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.code}'