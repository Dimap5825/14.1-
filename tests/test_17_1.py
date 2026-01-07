from unittest.mock import patch
import pytest
from tests.test_main import class_product_1, class_product_2, class_category
from src.product import Product


def test_zero_quantity_base_product():
    """
    Проверка создания обьекта класса Product с количеством = 0
    """
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        # обьект не используется потому что ошибка должна быть в момент создания(он не создастся)
        obj = Product(name= 'name', description= 'описание', price= 1, quantity= 0)

def test_category_middle_price(class_product_1, class_product_2, class_category):
    """
    Тест средне арифметического(просто что метод работает)
    :param class_product_1:
    Product(name="Cola", description="foreign", price=66, quantity=123)

    :param class_product_2:
    Product(name="Pepsi", description="foreign", price=66, quantity=123)

    :param class_category:
    Category(name="drinks", description="carbonated", products=[])

    :return:
    """
    with patch(target= 'builtins.input', return_value= 'y' ):
        product_1 = class_product_1
        # меняю для удобства
        product_1.price = 10
        product_1.quantity = 1

        # меняю для удобства
        product_2 = class_product_2
        product_2.price = 4
        product_2.quantity = 1

        category = class_category
        # добавляю продукты в категорию
        category.add_product([product_1,product_2])

        assert category.middle_price() == 7


def test_zero_quantity(class_category, class_product_1):
    """
    проверка работы метода Category.middle_price
    с делением на 0
    (quantity = 0 будет)
    :param class_category:
    :param class_product_1:
    :return:
    """
    category = class_category
    p_1 = class_product_1
    # тут ожидаю ошибку ValueError из сеттера Product
    with pytest.raises(ValueError, match= "Товар с нулевым количеством не может быть добавлен"):
        # при попытке изменить значение количества на 0 ожидаем ошибку
        p_1.quantity = 0
    # так как добавить продукт с количеством = 0 невозможно из-за сеттера проверяем категорию с пустым списком продуктов
    
    assert category.middle_price() == 0
