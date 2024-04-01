from src.product import Product


class Smartfone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 productivity: int, model: str, memory: int, color: str):
        self.productivity = productivity
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

