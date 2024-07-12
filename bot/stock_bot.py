import time
from threading import Thread

import yaml
from consumer import Consumer
from pyrabbit.api import Client


class StockBot:
    def __init__(self, host="localhost", port="15672", user="guest", passwd="guest"):
        self.host = host
        self.cli = Client("{}:{}".format(host, port), user, passwd)
        self.queues = []
        self.consumers = []

    def query_queues(self):
        return [q["name"] for q in self.cli.get_queues()]

    def start_working(self):
        while True:
            queues = self.query_queues()
            up = [q for q in list(set(queues) - set(self.queues)) if q[0] != "_"]
            threads = [
                Thread(target=Consumer(q, host=self.host).start_consuming) for q in up
            ]
            [t.start() for t in threads]
            self.consumers += threads
            self.queues += up
            print(self.queues)
            time.sleep(5)


def read_config_file():
    try:
        with open("config.yml", "r") as stream:
            yamlData = yaml.safe_load(stream)
            host = yamlData["rabbitmq-host"]
            port = yamlData["rabbitmq-port"]
            user = yamlData["rabbitmq-user"]
            passwd = yamlData["rabbitmq-pass"]
            return host, port, user, passwd
    except Exception:
        pass


if __name__ == "__main__":
    configs = read_config_file()
    if configs is None:
        stock_bot = StockBot()
    else:
        stock_bot = StockBot(*configs)
    stock_bot.start_working()
