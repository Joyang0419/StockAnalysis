import pandas as pd
from app.crawlers.crawler_daily_price_info import CrawlerDailyPriceInfo
from app.crawlers.crawler_stock_basic_info import CrawlerStockBasicInfo


class DataHandler:
    __handled_data: list

    def handle_stock_basic_info(self, crawler=CrawlerStockBasicInfo()):
        """整理股票基本資訊，output_data: [{stock_code, stock_name}]"""
        response_text = crawler.response.text
        dataframe = pd.read_html(response_text)[0]
        column_rename_dict = {
            '代號▼': 'stock_code',
            '名稱▼': 'stock_name',
        }
        dataframe.rename(columns=column_rename_dict, inplace=True)
        # 要留下的column
        select_columns_list = [value for key, value in column_rename_dict.items()]
        dataframe = dataframe[select_columns_list]
        self.__handled_data = dataframe.to_dict(orient='records')  # 資料格式: [{row_data}]
        return self.handled_data

    def handle_daily_price_info(self, crawler=CrawlerDailyPriceInfo()):
        """整理每日交易資訊，output_data: [{stock_basic_info_id, volume,
        closing_price, opening_price, highest_price, lowest_price}]"""
        response_text = crawler.response.text
        dataframe = pd.read_html(response_text)[0]
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
        self.__handled_data = dataframe.to_dict(orient='records')  # 資料格式: [{row_data}]
        return self.handled_data

    @property
    def handled_data(self):
        return self.__handled_data
