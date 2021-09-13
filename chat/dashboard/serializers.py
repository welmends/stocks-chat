from django.contrib.auth.models import User
from .models import Message
from rest_framework import serializers

class MessageSerializer(serializers.Serializer):
    text      = serializers.CharField()
    user_name = serializers.CharField()
    user_id   = serializers.IntegerField()
    room_name = serializers.CharField()
    room_id   = serializers.IntegerField()
    datetime  = serializers.CharField()