class Product_Service:
    LIST = []

    @classmethod
    def add_product(cls, product):
        cls.LIST.append(product)

    @classmethod
    def get_products(cls):
        return cls.LIST