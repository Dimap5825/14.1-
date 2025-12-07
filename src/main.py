# Задание 1
class Product:
    """
    Класс продукт
    """
    # название
    name : str
    # описание
    description : str
    # цена
    price : int
    # количество в наличии
    quantity : int
    # задание 2 инициализация
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    # позволяет сравнивать 2 обьекта
    def __eq__(self, other):
        # если класс не Product сравнивать смысла нет
        if not isinstance(other, Product):
            return False
        # если оба обьекта имеют класс Product то сравнивать их по параметрам
        return (
                self.name == other.name and
                self.description == other.description and
                self.price == other.price and
                self.quantity == other.quantity
        )

    # определяет как обьект будет выглядить при выходе
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
    def __init__(self, name, description, products = None ):
        # название
        self.name = name
        # описание
        self.description = description
        # список товаров
            #     если пустой
        if products is None:
            products = []
        self.products = products
        # количество товаров
        self.count_products = len(products)

        Category.count_category += 1
        Category.general_count_products += len(products)

    # правила сравнения
    def __eq__(self, other):
        # если тип обьекта не Category вернёт False b правила сравнения не будут работать
        if not isinstance(other,Category):
            return False

        # Если типы данных у обоих Category то сравниваем их по полям
        return (
            self.name == other.name and
            self.description == other.description and
            self.products == other.products
        )

     # чтобы выводилось красиво
    def __repr__(self):
        return (
                f'\n   Category(name = {self.name}, description = {self.description},'
                f'products = {self.products}, count_products = {self.count_products})\n'
                f'Всего категорий:{Category.count_category}\n'
                f'Всего продуктов:{Category.general_count_products})'
        )



# category_list = generate_category_list()
