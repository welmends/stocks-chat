from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    users = models.ManyToManyField(User)
    name = models.CharField(max_length=50)

class Message(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)