import pika

from worker import Worker


class Consumer(Worker):
    def __init__(self, queue, host="localhost"):
        super().__init__()
        self.host = host
        self.connection = None
        self.channel = None
        self.queue = queue

    def callback(self, ch, method, properties, body):
        status, response = self.stock_request(str(body.decode()))
        message = 'There is no such quote "{}"'.format(response["code"])
        if status:
            message = "{} quote is ${} per share".format(
                response["code"], response["price"]
            )

        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        channel = connection.channel()
        channel.queue_declare(queue="_{}".format(self.queue))
        channel.basic_publish(
            exchange="", routing_key="_{}".format(self.queue), body=message
        )
        connection.close()

    def start_consuming(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue)

        self.channel.basic_consume(
            queue=self.queue, on_message_callback=self.callback, auto_ack=True
        )
        self.channel.start_consuming()
