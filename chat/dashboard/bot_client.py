from threading import Thread
import pika
from django.contrib.auth.models import User
from .models import Room, Message

class BotClient(Thread):
    def __init__(self, room, stock_code, host='localhost'):
        super().__init__()
        self.host = host
        self.connection = None
        self.channel = None
        self.queue = room.name
        self.room_id = room.id
        self.stock_code = stock_code

    def callback(self, ch, method, properties, body):
        room = Room.objects.get(id=self.room_id)
        user = User.objects.get(username='bot')
        message = Message.objects.create(room=room, user=user, text=body.decode())
        message.save()
        
    def run(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=self.stock_code)
        self.connection.close()
        
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='_{}'.format(self.queue))
        self.channel.basic_consume(queue='_{}'.format(self.queue), on_message_callback=self.callback, auto_ack=True)
        self.channel.start_consuming()
