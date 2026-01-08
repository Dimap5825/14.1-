import abc

import pytest

from src.base_class import BaseProduct
from src.category import Category
from src.product import LawnGrass, Mixin, Product, Smartphone


@pytest.fixture()
def class_args():
    """
    1
    Вводные данные для теста класса Product
    :return: Product
    """

    return ["Cola", "foreign", 66, 123]


def test_create_baseclass(class_args):
    """
    Проверка на ошибку при создании обьекта абстрактного класса
    :return:
    """
    with pytest.raises(TypeError):
        obj = BaseProduct(*class_args)


def test_mro_baseclass():
    assert Smartphone.__mro__ == (
        Smartphone,
        Product,
        Mixin,
        BaseProduct,
        abc.ABC,
        object,
    )

    assert Category.__mro__ == (Category, object)
    assert Product.__mro__ == (Product, Mixin, BaseProduct, abc.ABC, object)
    assert LawnGrass.__mro__ == (
        LawnGrass,
        Product,
        Mixin,
        BaseProduct,
        abc.ABC,
        object,
    )


def test_console_massage_baseclass(capsys, class_args):
    """
    Проверяет вывод сообщения в консоль о создании нового обьекта в чьей родословной есть class Mixin
    :param class_args: ["Cola","foreign", 66, 123]
    # :return:
    """
    # переменная не используется, но в процессе создания в командную строку выводиться сообщение
    obj = Product(*class_args)
    cap = capsys.readouterr()
    assert (
        "Product(name = Cola,description = foreign,price = 66,quantity = 123)"
        in cap.out
    )
