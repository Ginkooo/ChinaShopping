import apps.provider_lister.providers.provider as provider
import apps.provider_lister.product.product as product
import urllib.request as request
from bs4 import BeautifulSoup

class AliexpressCrawler(provider.Provider):


    def fetch_offers(self):
        return [self.extract_product(), self.extract_product()]

    def extract_product(self, productlist):
        return product.Product("Dupsko", "htetepees", 69)
