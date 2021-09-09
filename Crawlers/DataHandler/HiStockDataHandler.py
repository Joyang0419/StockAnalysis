from Crawlers.DataHandler import DataHandler
from Crawlers import Crawler
import pandas as pd


class HiStockDataHandler(DataHandler):
    def pandas_read_html(self, crawler: Crawler):
        response_text = crawler.response().text
        table = pd.read_html(response_text)[0]
        return table
