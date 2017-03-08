import apps.provider_lister.providers.provider as provider
import apps.provider_lister.product.product as product

class AliexpressCrawler(provider.Provider):


    def fetch_offers(self):
        return [self.extract_product(), self.extract_product()]

    def extract_product(self):
        return product.Product("Jajko", "htetepees", 100)
