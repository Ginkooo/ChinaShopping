import apps.provider_lister.providers.provider as provider
import apps.provider_lister.product.product as product
from apps.provider_lister.connection.connection_request import ConnectionRequest
from apps.provider_lister.connection.connection_service import ConnectionService
import urllib.request as request
from bs4 import BeautifulSoup

class AliexpressCrawler(provider.Provider):

    def __init__(self, connection_service):
        self.__connection_service = connection_service

    def fetch_offers(self):
        connection_request = ConnectionRequest()
        connection_request.add_url("http://google.pl")
        response = self.__connection_service.execute(connection_request)
        return [self.extract_product("test"), self.extract_product("test")]

    def extract_product(self, productlist):
        return product.Product("Dupsko", "htetepees", 69)
