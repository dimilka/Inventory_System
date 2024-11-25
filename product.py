class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def is_valid(self):
        return isinstance(self.name, str) and self.name and self.quantity >= 0
