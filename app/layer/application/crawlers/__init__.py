from app.crawlers import Crawler
from app.crawlers.data_handler import DataHandlerAbstract
from app.models import ModelAbstract
import abc
from app.models import ModelAbstract


class ApplicationCrawlerAbstract(abc.ABC):

    @abc.abstractmethod
    def execute(self, crawler: Crawler, data_handler: DataHandlerAbstract, model: ModelAbstract):
        """執行爬蟲並將資料存入database"""
        raise NotImplementedError
