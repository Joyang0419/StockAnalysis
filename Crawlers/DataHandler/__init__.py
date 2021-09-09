import abc
from Crawlers import Crawler


class DataHandler(abc.ABC):
    @abc.abstractmethod
    def pandas_read_html(self, crawler: Crawler):
        raise NotImplementedError
