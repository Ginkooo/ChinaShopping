from django.db import models

class Product(models.Model):

    def __init__(self, name: str, price_in_dollars: float):
        self.name = name
        self.price_in_dollars = price_in_dollars
        print ("Product has been made!")
	