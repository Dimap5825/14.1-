from  config import DATA_PATH
from src.main import Product, Category
import json


def json_to_py_dict(path = DATA_PATH)->dict|list:
    """
    :param path:
    :return:
    """
    with open(DATA_PATH,'r') as f:
        return json.load(f)

# Дополниетльное задание

def generate_category_list(path:str=None) ->list:
    """
    Генерирует список категорий из json файла(json файл - источник)
    :param path:
    :return: список категорий
    """
    data_list = json_to_py_dict(path= path)
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

    return category_list

# print(generate_category_list())