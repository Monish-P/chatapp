from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    user = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    room = models.CharField(max_length=1000000)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + 'Profile'