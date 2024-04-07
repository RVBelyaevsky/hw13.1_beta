from src.product import Product


class Category:
    name: str
    description: str
    products: list

    count_categories = 0
    unique_products = 0


    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products
        self.count_categories = 1

        Category.count_categories += 1
        Category.unique_products += len(self.__products)


    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.products})"

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        sum_products = 0
        for i in self.__products:
            sum_products += i.quantity
        return sum_products


    @property
    def products(self):
        products_str = []
        for product in self.__products:
            products_str.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return products_str

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError('Невозможно добавить этот объект')
        elif product.quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен!")
        self.__products.append(product)
        Category.unique_products += 1

    def average_price(self):
        try:
            all_prices = []
            for product in self.__products:
                all_prices.append(product.price)
            return sum(all_prices) / len(all_prices)
        except ZeroDivisionError:
            return 0
