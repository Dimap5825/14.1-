class Product:
    """
    Класс продукт
    """

    # название
    name: str
    # описание
    description: str
    # цена
    price: int
    # количество в наличии
    quantity: int

    # задание 2 инициализация
    def __init__(self, name, description, price, quantity):

        self.name = name
        self.description = description
        # приватный
        self.__price = price
        self.quantity = quantity
        self.info = {
            "name": self.name,
            "description": self.description,
            "price": self.__price,
            "quantity": self.quantity,
        }
        self._is_initialized = True

    # строковое отображение продукта
    def __str__(self):
        """

        :return: str
        """
        return f"{self.name}, {self.__price} руб. Остаток:{self.quantity} шт.\n"

    def __add__(self, other):
        """
        сложение продуктов
        :param other:
        :return: int|float
        """
        return (self.price * self.quantity) + (other.price * other.quantity)

    # позволяет сравнивать 2 обьекта
    def __eq__(self, other):
        # если класс не Product сравнивать смысла нет
        if not isinstance(other, Product):
            return False
        # если оба обьекта имеют класс Product, то сравнивать их по параметрам
        return (
            self.name == other.name
            and self.description == other.description
            and self.price == other.price
            and self.quantity == other.quantity
        )

    # определяет как обьект будет выглядить при выходе
    def __repr__(self):
        return (f"Product(name = {self.name},"
                f"description = {self.description},"
                f"price = {self.price},"
                f"quantity = {self.quantity})")

    # Задание 3 (14.2)
    # Пусть нам передают список товаров в таом формате:
    # products = [
    #     Product(...),
    #     Product(...),
    # ]
    @classmethod
    def new_product(cls, data_dict, list_of_unique_products=None):
        # list_of_unique_products - список уникальных имён продуктов
        # (чтобы не повторялись по заданию даётся сам по себе)
        # Создаём новый обьект
        new_product = cls(
            name=data_dict["name"],
            description=data_dict["description"],
            price=data_dict["price"],
            quantity=data_dict["quantity"],
        )
        # Начинаем проверку в переданном списке если передан
        if list_of_unique_products:
            # Если есть продукт с таким именем, то меняем информацию о его количестве
            for product in list_of_unique_products:
                # если имя такое же то начинаем обьединять
                if product.name == new_product.name:
                    product.quantity += new_product.quantity
                    if product.price < new_product.price:
                        product.price = new_product.price
                    new_product = product
                    return new_product
            # если не нашлось продукта с таким именем, то код дойдёт до сюда
            list_of_unique_products.append(new_product)
        return new_product

    # Задание 4 геттер для Product.__price
    # Задание 4

    # в случае если цена равна или ниже нуля, выводите сообщение в консоль
    # “Цена не должна быть нулевая или отрицательная”
    # при этом новую цену устанавливать не нужно.
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int | float = 0):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if self.__price > new_price:
                # запуск цикла для получения ответа от пользователя
                while True:
                    # если цену хотят снизить запрагиваем ращрешение
                    user_answer = input(
                        "Вы хотите понизить цену?\ny (значит yes) или n (значит no) "
                    )
                    # если да меняем цену
                    if user_answer.lower() == "y":
                        self.__price = new_price
                        break
                    elif user_answer.lower() == "n":
                        print("Изменение цены отменено")
                        break
                    else:
                        print("неверный ввод, попробуйте заново")

    @property
    def display(self):
        return self.__str__()
