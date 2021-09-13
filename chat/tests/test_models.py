from django.test import TestCase
from django.contrib.auth.models import User
from dashboard.models import Room, Message
from django.contrib.auth.hashers import make_password

class RegistrationTests(TestCase):
    def test_models_fields(self):
        user = User()
        user.username = '<user_name>'
        user.password = make_password('<passwd>')
        user.save()

        record = User.objects.get(username=user.username)
        self.assertEqual(record, user)
        
class DashboardTests(TestCase):
    def test_models_fields(self):
        room = Room()
        room.name = '<room_name>'
        room.save()

        record = Room.objects.get(pk=1)
        self.assertEqual(record, room)

        message = Message()
        message.text = '<message_text>'
        message.user = User.objects.get(username='user')
        message.room = room
        message.save()

        record = Message.objects.get(pk=1)
        self.assertEqual(record, message)