from threading import Thread
from pyrabbit.api import Client
import time
from consumer import Consumer

class StockBot:
    def __init__(self, host='localhost', port='15672', user='guest', passwd='guest'):
        self.cli = Client('{}:{}'.format(host, port), user, passwd)
        self.queues = []
        self.consumers = []

    def query_queues(self):
        return [q['name'] for q in self.cli.get_queues()]

    def start_working(self):
        while(True):
            queues = self.query_queues()
            up = [q for q in list(set(queues) - set(self.queues)) if q[0]!='_']
            threads = [Thread(target=Consumer(q).start_consuming) for q in up]
            [t.start() for t in threads]
            self.consumers += threads
            self.queues += up
            print(self.queues)
            time.sleep(5)


if __name__ == '__main__':
    stock_bot = StockBot()
    stock_bot.start_working()