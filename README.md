# Python, OOP

Учебный проект на Python с использованием объектно-ориентированного программирования, Poetry, pytest и контроля покрытия кода.

## 📌 Описание проекта

Проект реализует:
- работу с товарами и категориями;
- наследование и перегрузку операторов;
- загрузку данных из JSON;
- валидацию типов;
- автоматические тесты с покрытием кода более **75%**.

## 📂 Структура проекта
```bash
.
├── config.py
├── data.json
├── src/
│ ├── auxiliary_functions.py
│ ├── category.py
│ ├── product.py
│ ├── main.py
│ └── init.py
├── tests/
│ ├── test_main.py
│ ├── test_generate_category_list.py
│ └── init.py
├── htmlcov/
├── pyproject.toml
├── poetry.lock
└── README.md
```
# ⚙️ Установка и запуск

```bash
poetry install
poetry shell
python src/main.py
```
## Тестирование
```bash
pytest
pytest --cov=src --cov-report=html
```
Отчет html

htmlcov/index.html

# Примеры использования
```bash
# Импорт классов
from src.product import Smartphone, LawnGrass
from src.category import Category
from src.auxiliary_functions import generate_category_list

# Создание объектов
smartphone1 = Smartphone("iPhone 15", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray")
smartphone2 = Smartphone("Samsung S23", "256GB", 180000.0, 5, 95.5, "S23", 256, "Black")
grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

# Доступ к атрибутам
print(smartphone1.name)
print(smartphone2.price)
print(grass.country)

# Сложение товаров одного типа
result = smartphone1 + smartphone2
print(result)

# Ошибка при сложении разных типов
# smartphone1 + grass  # TypeError

# Работа с категориями
category = Category("Смартфоны", "Высокотехнологичные устройства", [smartphone1, smartphone2])
category.add_product(smartphone1)
print(category.products)

# Ошибка при добавлении объекта не типа Product
# category.add_product("not a product")  # TypeError

# Генерация категорий из JSON
categories = generate_category_list()
for cat in categories:
    print(cat.name)
```

# 📦 Используемые технологии
```bash
Python 3.13

Poetry

pytest

pytest-cov
```
# 👤 Автор

Dimap5825

