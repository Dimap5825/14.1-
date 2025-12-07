            # Задание 3
# Напишите тесты для классов, которые проверяют:
    #     корректность инициализации объектов класса
    #     Category, корректность инициализации объектов класса
    #     Product, подсчет количества продуктов, подсчет количества категорий.
import  pytest
from src.main import Category,Product

@pytest.fixture()
def class_Category():
    """
    Вводные данные для теста класса Category
    :return:Category
    """
    Category.count_category = 0
    Category.general_count_products = 0
    return Category(name= 'drinks', description= 'carbonated', products= ['Cola', 'Pepsi', 'Mirinda'] )


@pytest.fixture()
def class_Product():
    """
    Вводные данные для теста класса Product
    :return: Product
    """

    Category.count_category = 0
    Category.general_count_products = 0
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


def test_category_with_products():
    # создаём продукты
    p1 = Product("Хлеб", "Свежий", 50, 10)
    p2 = Product("Молоко", "1л", 70, 5)

    # создаём категорию с продуктами
    cat = Category("Продукты", "Еда", [p1, p2])

    assert cat.name == "Продукты"
    assert cat.description == "Еда"
    assert cat.count_products == 2
    assert cat.products == [p1, p2]

def test_category_without_products():
    # создаём категорию без передачи списка продуктов
    cat = Category("Пустая", "Нет продуктов")

    assert cat.name == "Пустая"
    assert cat.description == "Нет продуктов"
    assert cat.count_products == 0
    assert cat.products == []