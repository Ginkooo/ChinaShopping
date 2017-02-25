import apps.providers.product_service as product


class Provider:

    def fetch_offers(self):
        raise NotImplementedError()

    @staticmethod
    def add_product(prod):
        product.Product_Service.add_product(prod)

    def extract_product(self):
        raise NotImplementedError()

