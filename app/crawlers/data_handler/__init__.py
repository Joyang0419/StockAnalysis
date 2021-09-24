import abc
from app.crawlers import Crawler
# from app.models import ModelAbstract


class DataHandlerAbstract(abc.ABC):
    handled_data: list

    @abc.abstractmethod
    def handle_data(self, crawler: Crawler):
        """資料整理"""
        raise NotImplementedError
