class Product:
    name: str
    description: str
    price: float
    quantity: int
    instances = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.instances.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity


    @classmethod
    def create_product(cls, new_product: dict):
        instance = cls(**new_product)
        return instance

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('цена введена некорректная')
        else:
            self.__price = new_price
