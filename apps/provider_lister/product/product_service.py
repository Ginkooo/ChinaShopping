class Product_Service:
    PRODUCTS = []

    @classmethod
    def add_products(cls, products):
        cls.PRODUCTS.extend(products)

    @classmethod
    def get_products(cls):
        return cls.PRODUCTS

    @classmethod
    def clear_products(cls):
        cls.PRODUCTS.clear()
