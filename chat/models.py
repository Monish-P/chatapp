from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000,blank=True)
    user = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=1000000)
    image = models.ImageField(default='',upload_to='chat_imgs',blank=True)
    def __str__(self):
        return 'message'+str(self.id)
class Profile(models.Model):
    user=models.OneToOneField(User,related_name='Profile',on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    is_online = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username + 'Profile'

class Notification(models.Model):
    user = models.CharField(max_length=1000000)

    def __str__(self):
        return 'Message from '+self.user

class Group(models.Model):

    name = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000000)