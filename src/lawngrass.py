from src.product import Product

class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    # def __str__(self):
    #     return f"{self.name}, {self.description}, {self.price}, {self.quantity}, {self.country}, {self.germination_period}, {self.color}"