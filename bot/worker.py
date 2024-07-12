import csv

import requests


class Worker:
    def __init__(
        self, uri="https://stooq.com/q/l/?s={stock_code}&f=sd2t2ohlcv&h&e=csv​"
    ):
        self.uri = uri

    def stock_request(self, code):
        try:
            uri = self.uri.format(stock_code=code)
            download = requests.get(uri)
            stock = list(
                csv.reader(download.content.decode("utf-8").splitlines(), delimiter=",")
            )
            response = {
                "code": stock[1][stock[0].index("Symbol")],
                "price": stock[1][stock[0].index("Close")],
            }
            return True if response["price"] != "N/D" else False, response
        except Exception:
            return False, {"code": code, "price": "N/D"}
