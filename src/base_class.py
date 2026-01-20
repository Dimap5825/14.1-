from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный Базовый класс(родительский)
    """

    __slots__ = ("name", "description", "price", "quantity")

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        # предварительные проверки
        ## если количество 0 то ошибка Товар с нулевым количеством не может быть добавлен
        # if quantity == 0:
        #     raise ValueError("Товар с нулевым количеством не может быть добавлен")

        # создание обьекта
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
