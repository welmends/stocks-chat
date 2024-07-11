from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=50)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
