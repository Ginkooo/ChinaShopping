class Product:

    id = 0

    def __init__(self, name: str, price_in_dollars: float):
        self.name = name
        self.price_in_dollars = price_in_dollars
        Product.id += 1
        print ("Product has been made!")

    def __repr__(self):
        return "product {}".format(self.name)
