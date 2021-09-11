import abc
from Crawlers import Crawler


class DataHandler(abc.ABC):
    __crawler: Crawler

    @abc.abstractmethod
    def main(self):
        raise NotImplementedError
