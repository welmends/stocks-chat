from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Message


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField()
    user_name = serializers.CharField()
    user_id = serializers.IntegerField()
    room_name = serializers.CharField()
    room_id = serializers.IntegerField()
    datetime = serializers.CharField()
