import requests


class Crawler:
    url = ''
    method = ''
    headers = {}
    __response = ''

    def __init__(self, url: str, method: str, headers_string: str):
        self.url = url
        self.method = method
        self.headers = self.headers_handlers(headers_string)
        self.__response = self.request()

    def request(self):
        request = getattr(requests, self.method)
        return request(self.url, headers=self.headers)

    def headers_handlers(self, input_string: str):
        for each_line in input_string.split('\n'):
            self.headers[each_line.split(': ')[0]] = each_line.split(': ')[1]
        return self.headers

    def response(self):
        return self.__response
