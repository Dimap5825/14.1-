            # Задание 3
# Напишите тесты для классов, которые проверяют:
#     корректность инициализации объектов класса
#     Category, корректность инициализации объектов класса
#     Product, подсчет количества продуктов, подсчет количества категорий.
import  pytest
from main import Category,Product


@pytest.fixture()
def class_Category():
    """
    Вводные данные для теста класса Category
    :return:Category
    """
    return Category(name= 'drinks', description= 'carbonated', products= ['Cola', 'Pepsi', 'Mirinda'] )

@pytest.fixture()
def class_Product():
    """
    Вводные данные для теста класса Product
    :return: Product
    """
    return Product(name='Cola', description='foreign' , price=66, quantity=123)


def test_class_Category(class_Category):
    '''
    проверка инициализации Category
    :param class_Category:
    :return:
    '''
    assert class_Category.name == 'drinks'
    assert class_Category.description == 'carbonated'
    assert class_Category.products == ['Cola', 'Pepsi', 'Mirinda']
    assert class_Category.count_products == 3
    assert class_Category.count_category == 1


def test_class_Product(class_Product):
    assert  class_Product.name == 'Cola'
    assert class_Product.description == 'foreign'
    assert class_Product.price == 66
    assert  class_Product.quantity == 123
