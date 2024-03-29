# import json
# from config import products_path
#
# with open(products_path, encoding='utf-8') as file:
#     data = file.read()
# test_data = json.loads(data)


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
        self.__products.append(product)
        Category.unique_products += 1


class Product:
    name: str
    description: str
    price: float
    quantity: int
    instances = []

    def __init__(self, name, description, price, quantity):
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


product_1 = Product('nokia', 'good telephone', 100.0, 10)
product_2 = Product('sony', 'no good telephone', 200.0, 2)
# product_1.price = 0
# print(product_1.price)
#
products_list = [product_1, product_2]
# print(products_list)
#
category_1 = Category('telephones', 'old telephones', products_list)
# print(category_1)
#
# print(category_1.products)
# # for category in test_data:
# #     category_list.append(Category(category['name'], category['description'], category['products']))
# print(Category.count_categories)
# print(Category.unique_products)
# # print(category_list[0].name, "---", category_list[0].description)
# # print(category_list[1].name, "---", category_list[1].description)
# # print(category_list[0])
# #
# #
# # new_product = Product('a', 'b', 150.0, 20)
# #
# # category_list[0].add_product(new_product)
# # print(Category.count_categories)
# # print(Category.unique_products)
# # print(category_list[1])
#
# new_product = {
#         "name": "Iphone 15",
#         "description": "512GB, Gray space",
#         "price": 210000.0,
#         "quantity": 8
#       }
# print(product_1.instances)
# product_1.create_product(new_product)
# print(product_1.instances)

print(str(product_1))
print(str(product_2))
print(str(category_1))
print(product_1 + product_2)
