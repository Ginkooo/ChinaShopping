import apps.providers.provider as provider
import apps.providers.product as product

class AliExpressCrawler(provider.Provider):

    id = 0

    def fetch_offers(self):
        return [self.extract_product(), self.extract_product()]

    def extract_product(self):
        return product.Product("Jajko", 2)