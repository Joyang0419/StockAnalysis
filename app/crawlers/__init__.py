import requests


class Crawler:
    url = ''
    method = ''
    headers = {}
    __response = ''

    def __init__(self, url: str, method: str, headers_string: str):
        self.url = url
        self.method = method
        self.headers = self.__handle__headers(headers_string)
        self.__request()

    def __request(self):
        request_method = getattr(requests, self.method)
        self.__response = request_method(self.url, headers=self.headers)

    def __handle__headers(self, input_string: str):
        for each_line in input_string.split('\n'):
            self.headers[each_line.split(': ')[0]] = each_line.split(': ')[1]
        return self.headers

    @property
    def response(self):
        return self.__response

