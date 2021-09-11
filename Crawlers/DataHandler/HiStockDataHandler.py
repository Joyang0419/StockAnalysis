from Crawlers.DataHandler import DataHandler
from Crawlers import Crawler
import pandas as pd


class HiStockDataHandler(DataHandler):
    __dataframe: pd.DataFrame
    __crawler: Crawler

    def __init__(self, crawler: Crawler):
        self.__crawler = crawler

    def __pandas_read_html(self) -> None:
        """html's table轉成dataframe"""
        response_text = self.__crawler.response().text
        self.__dataframe = pd.read_html(response_text)[0]

    def __handle_dataframe(self) -> None:
        """整理成需要的dataframe"""
        # rename column: stock_code(代號▼), stock_name(名稱▼) ,volume(成交量▼),
        # lowest(最低▼), highest(最高▼), opening(開盤▼), closing(價格▼)
        column_rename_dict = {
            '代號▼': 'stock_code',
            '名稱▼': 'stock_name',
            '成交量▼': 'volume',
            '價格▼': 'closing',
            '開盤▼': 'opening',
            '最高▼': 'highest',
            '最低▼': 'lowest',
        }
        self.__dataframe.rename(columns=column_rename_dict, inplace=True)
        # 要留下的column
        select_columns_list = [value for key, value in column_rename_dict.items()]
        self.__dataframe = self.__dataframe[select_columns_list]

    def __display_dataframe(self):
        return self.__dataframe

    def main(self) -> object:
        self.__pandas_read_html()
        self.__handle_dataframe()
        return self.__display_dataframe()
