from app.crawlers.data_handler import DataHandlerAbstract
from app.crawlers import Crawler
import pandas as pd
# from app.models.daily_price_info import DailyPriceInfo


class HiStockDataHandler(DataHandlerAbstract):
    __dataframe: pd.DataFrame

    def __init__(self):
        pass

    def handle_data(self, crawler: Crawler):
        response_text = crawler.response().text
        dataframe = pd.read_html(response_text)[0]
        handled_dataframe = self.__handle_dataframe(dataframe)
        self.handled_data = handled_dataframe.to_dict(orient='records')  # 資料格式: [{row_data}]

    @staticmethod
    def __handle_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
        """整理成需要的dataframe"""
        # rename column: stock_code(代號▼), stock_name(名稱▼) ,volume(成交量▼),
        # lowest(最低▼), highest(最高▼), opening(開盤▼), closing(價格▼)
        column_rename_dict = {
            '代號▼': 'stock_code',
            '名稱▼': 'stock_name',
            '成交量▼': 'volume',
            '價格▼': 'closing_price',
            '開盤▼': 'opening_price',
            '最高▼': 'highest_price',
            '最低▼': 'lowest_price',
        }
        dataframe.rename(columns=column_rename_dict, inplace=True)
        # 要留下的column
        select_columns_list = [value for key, value in column_rename_dict.items()]
        dataframe = dataframe[select_columns_list]
        return dataframe
