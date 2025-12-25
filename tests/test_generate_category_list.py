from src.auxiliary_functions import generate_category_list
from src.main import Category, Product


def test_category_list():

    Category.count_category = 0  # сбрасываем глобальный счётчик
    Category.count_products = 0

    result = generate_category_list()

    expected = [
        Category(
            name="Смартфоны",
            description="Смартфоны, как средство не только коммуникации,"
                        " но и получение дополнительных функций для удобства жизни",
            products=[
                Product(
                    name="Samsung Galaxy C23 Ultra",
                    description="256GB, Серый цвет, 200MP камера",
                    price=180000.0,
                    quantity=5,
                ),
                Product(
                    name="Iphone 15",
                    description="512GB, Gray space",
                    price=210000.0,
                    quantity=8,
                ),
                Product(
                    name="Xiaomi Redmi Note 11",
                    description="1024GB, Синий",
                    price=31000.0,
                    quantity=14,
                ),
            ],
        ),
        Category(
            name="Телевизоры",
            description="Современный телевизор,"
                        " который позволяет наслаждаться просмотром, "
                        "станет вашим другом и помощником",
            products=[
                Product(
                    name='55" QLED 4K',
                    description="Фоновая подсветка",
                    price=123000.0,
                    quantity=7,
                )
            ],
        ),
    ]

    assert result == expected
