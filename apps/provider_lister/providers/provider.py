import apps.provider_lister.product as product


class Provider:

    def fetch_offers(self):
        raise NotImplementedError()

    @staticmethod
    def add_product(products):
        product.Product_Service.add_products(products)

    def extract_product(self):
        raise NotImplementedError()
