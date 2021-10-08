from . import test
from app.crawlers import Crawler
from app.crawlers.data_handler.data_handler_for_hi_stock import DataHandlerForHiStock
from app.layer.application.application_crawler import ApplicationCrawler
from app.repositories.repository_stock_basic_info import RepositoryStockBasicInfo
from app import db
from app.models.stock_basic_info import StockBasicInfo


@test.cli.command('test_crawler_hi_stock')
def test_crawler_hi_stock():
    hi_stock_crawler = Crawler(
        url='https://histock.tw/stock/rank.aspx?p=all',
        method='get',
        headers_string="""authority: histock.tw
method: GET
path: /stock/rank.aspx
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
cache-control: max-age=0
cookie: _ga=GA1.2.726332527.1618810721; __gads=ID=368f7886ce599c0c-22681eeb7dc70095:T=1618810721:RT=1618810721:S=ALNI_MYZjvgsqlmdyczpzcTyRNvES3-5ug; ASP.NET_SessionId=2rbnoeks30od0tss245aek2b; _gid=GA1.2.766026611.1630920782; _gcl_au=1.1.902003577.1630920782; _fbp=fb.1.1630920782752.1915117014; _gat=1
sec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"""
    )
    print('=======================')
    print(hi_stock_crawler.response)
    print('=======================')

    application_crawler = ApplicationCrawler()
    data_handler = DataHandlerForHiStock(crawler=hi_stock_crawler)
    # data_handler.handle_data(data_type='stock_basic_info')
    # print(data_handler.provide_handled_data())
    repository = RepositoryStockBasicInfo(session=db.session, model=StockBasicInfo)
    application_crawler.crawl_stock_basic_info(data_handler=data_handler, repository=repository)


# hi_stock_data_handler = HiStockDataHandler()
# hi_stock_data_handler.handle_data(hi_stock_crawler)
# print(hi_stock_data_handler.get_handled_data())