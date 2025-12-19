import  pytest
from src.main import Category,Product


@pytest.fixture()
def class_product_1():
    """
    1
    Вводные данные для теста класса Product
    :return: Product
    """

    return Product(name='Cola', description='foreign' , price=66, quantity=123)

@pytest.fixture()
def class_product_2():
    """
    2
    Вводные данные для теста класса Product
    :return:Product
    """
    return Product(name='Pepsi', description='foreign', price=66, quantity=123)

# Шаблон категория
@pytest.fixture()
def class_category():
    """
    Вводные данные для теста класса Category(Список продуктов пустой)
    :return:Category
    """
    Category.count_category = 0
    Category.general_count_products = 0
    return Category(name= 'drinks', description= 'carbonated', products= [] )


@pytest.fixture()
def dict_for_create_product():
    """
    Словарь для создания обьекта типа Product
    :return:dict
    """
    return {'name':'Mirinda', 'description':'foreign' , 'price':66, 'quantity':123}



def test_class_category(class_category):
    """
    проверка инициализации Category
    :param class_category:
    :return:
    """

    assert class_category.name == 'drinks'
    assert class_category.description == 'carbonated'
    assert class_category.count_products == 0
    assert class_category.count_category == 1


def test_class_product(class_product_1):

    assert class_product_1.name == 'Cola'
    assert class_product_1.description == 'foreign'
    assert class_product_1.price == 66
    assert class_product_1.quantity == 123


def test_category_with_products():
    # создаём продукты
    p1 = Product("Хлеб", "Свежий", 50, 10)
    p2 = Product("Молоко", "1л", 70, 5)

    # создаём категорию с продуктами
    cat = Category("Продукты", "Еда", [p1, p2])

    assert cat.name == "Продукты"
    assert cat.description == "Еда"
    assert cat.count_products == 2


def test_category_without_products():
    # создаём категорию без передачи списка продуктов
    cat = Category("Пустая", "Нет продуктов")

    assert cat.name == "Пустая"
    assert cat.description == "Нет продуктов"
    assert cat.count_products == 0


# Задание 5 (14.2)
def test_private_attribute(class_category, class_product_1):
    """
    Проверка приватности аттрибуты .__products при обращении жду AttributeError
    :param class_category:
    :param class_product_1:
    :return: AttributeError
    """
    class_category.add_product(product=class_product_1)
    cat = class_category
    product = class_product_1
    cat.add_product(product)
    # проверка приватности ( что атрибут реально приватный)
    with pytest.raises(AttributeError):
        _ = cat.__products

def test_add_products(class_product_1, class_product_2, class_category):
    """

    Проверка метода Category.add_products

    :param class_product_1:
    :param class_product_2:
    :param class_category:
    :return:
    """
    # Создал категорию
    cat = class_category
    # Category(name='drinks', description='carbonated', products=[])
    # Создал продукт 1
    p_1 = class_product_1
    # Создал продукт 2
    p_2 = class_product_2
    # Product(name='Cola', description='foreign', price=66, quantity=123)
    # Запускаю метод .add_product
    cat.add_product(product=[p_1,p_2])

    assert cat.products == f'Cola, 66 руб. Остаток:123 шт.\nPepsi, 66 руб. Остаток:123 шт.\n'

def test_new_product(dict_for_create_product):
    """
       Проверка метода new_product
    :param dict_for_create_product:
    :return:
    """
    p_1 = Product.new_product(dict_for_create_product)
    # Обьект имеет класс Product
    assert type(p_1) == Product
    # Можно обращаться к атрибутам обьекта
    assert p_1.name == "Mirinda"

def test_new_product_2(dict_for_create_product):
    # Лист с продуктом из словаря
    list_for_test = [Product.new_product(dict_for_create_product)]
    # такой же продукт с такими же данными значит цена больше в 2 раза
    p_1 = Product.new_product(dict_for_create_product, list_of_unique_products=list_for_test)
    assert p_1.quantity == 246
    assert p_1.price == 66

def test_private_price_attribute_product(class_product_1):
    """
    Проверка приватности атрибута .price в классе Product
    :param class_product_1:
    :return:
    """
    p_1 = class_product_1
    with pytest.raises(AttributeError):

        _ = p_1.__price

# тест для
#  * Дополнительное задание (к заданию 4)
# В случае если цена товара понижается, добавить логику подтверждения пользователем
# вручную через ввод y (значит yes) или n (значит no) для согласия понизить цену
#  или для отмены действия соответственно.
def test_price_low_y(class_product_1,monkeypatch):
    """
    Проверка работы сеттера при ответе да
    (если цена понижается запрашивать подтверждение)
    :return:
    """
    # при ответе да
    # подменяем input → всегда отвечает "y"
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    p_1 = class_product_1 #price=66
    p_1.price = 19

    assert p_1.price == 19


def test_price_low_n(class_product_1, monkeypatch):
    """
    Проверка работы сеттера при ответе нет(в высоком регистре) "N"
    (если цена понижается запрашивать подтверждение)
    :return:
    """
    # подменяем input → всегда отвечает "n"
    monkeypatch.setattr('builtins.input', lambda _: 'N')

    p_1 = class_product_1  # price=66
    p_1.price = 19

    assert p_1.price == 66

