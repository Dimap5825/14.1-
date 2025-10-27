from auxiliary_functions import json_to_py_dict


# Задание 1
class Product:
    """
    Класс продукт
    """
    # название
    name : str
    # описание
    description:str
    # цена
    price:int
    # количество в наличии
    quantity:int
    # задание 2 инициализация
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'Product(name = {self.name}, description = {self.description},price = {self.price},quantity = {self.quantity})'


class Category:
    """
    Класс Категория
    """
    count_category = 0
    general_count_products = 0
    # название
    name:str
    # описание
    description:str
    # список товаров категории
    products:list
    # задание 2 инициализация
    def __init__(self, name, description, products ):
        self.name = name
        self.description = description
        self.products = products
        self.count_products = len(products)
        Category.count_category += 1
        Category.general_count_products += len(products)

     # чтобы выводилось красиво
    def __repr__(self):
        return (f'Category(name = {self.name}, description = {self.description},products = {self.products}, count_products = {self.count_products})\n'
                f'Всего категорий:{Category.count_category}\nВсего продуктов:{Category.general_count_products})\n')


# Дополниетльное задание


data_list = json_to_py_dict()
category_list = []
# Получаем словарь категории
for category in data_list:
    products_list = []
    for product in category['products']:
        products_list.append(Product
            (
            name=product['name'],
            description=product['description']
            ,price=product['price'],
            quantity=product['quantity']
            )
        )
        # print(products_list)
    category_list.append(Category(
        name=category['name'],
        description=category['description'],
        products=products_list
    ))


# print(data_list)
# print(category_list)
