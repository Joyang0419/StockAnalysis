from . import ApplicationCrawlerAbstract
from app.models.stock_basic_info import StockBasicInfo
from app.crawlers.data_handler.hi_stock_data_handler import HiStockDataHandler
from app.crawlers import Crawler


class ApplicationHiStock(ApplicationCrawlerAbstract):

    def execute(self, crawler: Crawler, data_handler: HiStockDataHandler, model: StockBasicInfo):
        data_handler.handle_data(crawler=crawler)
        for i in data_handler.handled_data:
            print(i)
            model.create(i)
            break
        pass




