from src.product import Product


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country_from: str, grown_time: float, color: str):
        super().__init__(name, description, price, quantity)
        self.country_from = country_from
        self.grown_time = grown_time
        self.color = color


