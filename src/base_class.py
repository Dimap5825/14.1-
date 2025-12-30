from abc import ABC,abstractmethod


class BaseProduct(ABC):
     """
     Абстрактный Базовый класс(родительский)
     """

     __slots__ = ('name', 'description', 'price', 'quantity')

     @abstractmethod
     def __init__(self, name, description, price, quantity):
         self.name = name
         self.description = description
         self.price = price
         self.quantity = quantity

