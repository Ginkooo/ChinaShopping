from bs4 import BeautifulSoup

class ConnectionResponse:

    def __init__(self, response):
        self.__response = response
        self.__html = response.read()
        self.__response_code = response.getcode()

    def get_as_beautiful_soup(self):
        bs = BeautifulSoup(self.html)
        return bs

    def get_html(self):
        return self.__html
