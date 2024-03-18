import json
from config import products_path

with open(products_path, encoding='utf-8') as file:
    data = file.read()
test_data = json.loads(data)


class Category:
    name: str
    description: str
    products: list

    count_categories = 0
    unique_products = 0
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.count_categories = 1

        Category.count_categories += 1
        Category.unique_products = len(self.products)


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# category_list = []
# for category in test_data:
#     category_list.append(Category(category['name'], category['description'], category['products']))
# print(Category.count_categories)
# print(category_list)