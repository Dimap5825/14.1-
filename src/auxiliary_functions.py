import json

from config import DATA_PATH
from src.category import Category
from src.product import Product


def json_to_py_dict(path=DATA_PATH) -> dict | list:
    """
     :param: path(путь к файлу .json)

     :return:list
     пример ниже
     [
    Category(
        name =
        description =
        products =
        [
            Product(
                name = ,
                description = ,
                price = ,
                quantity = ),
             Product(
                 name =
                 description = ,
                 Gray space,
                 price = ,
                 quantity = )
         ],
     Category(
     ...
     )
     ]

    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# Дополниетльное задание


def generate_category_list(path: str = DATA_PATH) -> list:
    """
    Генерирует список категорий из json файла(json файл - источник)
    :param path:
    :return: список категорий
    """
    data_list = json_to_py_dict(path=path)
    category_list = []
    # Получаем словарь категории
    for category in data_list:
        products_list = []
        for product in category["products"]:
            products_list.append(
                Product(
                    name=product["name"],
                    description=product["description"],
                    price=product["price"],
                    quantity=product["quantity"],
                )
            )
            # print(products_list)
        category_list.append(
            Category(
                name=category["name"],
                description=category["description"],
                products=products_list,
            )
        )

    return category_list


# print(generate_category_list())
