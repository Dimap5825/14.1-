from src.expected_category import CategoryExpected
from src.product import Product


class Category:
    """
    Класс Категория
    """

    # количсетво категорий
    category_count = 0
    # количетво продуктов
    product_count = 0
    # название
    name: str
    # описание
    description: str
    # список товаров категории
    products: list

    # задание 2 инициализация
    def __init__(self, name, description, products=None):
        # название
        self.name = name
        # описание
        self.description = description
        # список товаров
        if products is None:
            products = []
        self.__products = products
        # количество товаров
        self.product_count = len(products)

        Category.category_count += 1
        Category.product_count += len(products)

    # строковое отображение Category
    def __str__(self):
        """

        :return: str | формат по заданию:"Название категории, количество продуктов: 200 шт."
        """
        # алгоритм проходиться по всем продуктам в категории и складывает их количество
        total_quantity = 0
        for i in self.__products:
            total_quantity += i.quantity

        return f"{self.name}, количество продуктов: {total_quantity} шт."

    # правила сравнения
    def __eq__(self, other):
        # если тип обьекта не Category вернёт False b правила сравнения не будут работать
        if not isinstance(other, Category):
            return False

        # Если типы данных у обоих Category, то сравниваем их по полям
        return (
            self.name == other.name
            and self.description == other.description
            and self.__products == other.__products
        )

    # чтобы выводилось красиво для разработчика
    def __repr__(self):
        return (
            f"\n   Category(name = {self.name}, description = {self.description},"
            f"products = {self.__products}, count_products = {self.product_count})\n"
            f"Всего категорий:{Category.category_count}\n"
            f"Всего продуктов:{Category.product_count})"
        )

    # задание 1 (14.2)
    # добавить продукт
    def add_product(self, product: list[Product] | Product):
        """
        Добавление продукта в список категории
        self: категория(конкретная)
        product : список обьектов типа Product или просто обьект Product
        """
        try:
            # если передан просто обьект типа Product
            if isinstance(product, Product):
                self.__products.append(product)
                type(self).product_count += 1

            # если передан список с обьектами типа Product
            elif isinstance(product, list):
                for i in product:
                    # если i(обьект из списка) является обьектом класса Product или его наследников(дочерних классов)
                    if issubclass(type(i), Product):
                        if i.quantity == 0:
                            raise CategoryExpected(
                                "Товар с нулевым количеством не может быть добавлен"
                            )
                        # добавить обьект(i) в категорию
                        self.__products.append(i)
                        # количество продуктов +1
                        type(self).product_count += 1
            # если обьект не Product или его наследник
            else:
                raise TypeError
        except CategoryExpected as e:
            print(f"Ошибка : {e}")
        except TypeError:
            print("Ошибка: неверный тип обьекта")
        finally:
            print("Обработка добавления товара завершена")

    #     Задание 2(14.2)
    # Так как вы сделали атрибут со списком товаров приватным,
    # то атрибут «список товаров категории» у вас освободился,
    # но вы лишили программу возможности выводить список товаров.
    # Чтобы вернуть возможность просмотра товаров, нужно реализовать
    # Геттер
    # который будет выводить список товаров в виде строк в формате:
    # "Название продукта, 80 руб. Остаток: 15 шт."

    # свойство(геттер)
    def get_products(self):
        """

        :return: str (общая строка в формате как будто отдельные строки)
        """

        # генератор перебирающий по одному продукту в списке категории
        gener_product = (product.display for product in self.__products)
        return "".join(gener_product)

    # метод(заменяющий атрибут, потому что мы его сделали приватным)
    @property
    def products(self):
        """

        :return: str
        """
        return self.get_products()

    def middle_price(self):
        """
        метод подсчитывает средний ценник товаров внутри категории
        return:
        """
        # общая сумма
        sum_price = 0
        # общее количество
        sum_quantity = 0
        try:

            for product in self.__products:
                sum_price += product.price * product.quantity
                sum_quantity += product.quantity

            # средняя цена 1 товара внутри категории
            return sum_price / sum_quantity

        except ZeroDivisionError:
            return 0


# p_1 = Product('name','описание',99,2)
# print(p_1)
