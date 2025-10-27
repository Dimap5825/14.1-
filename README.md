# 🛍️ Homework 14.1 — Классы Product и Category

Этот проект демонстрирует работу с классами в Python и взаимодействие с JSON-данными.  
В нём реализованы два основных класса — **Product** и **Category**, а также модуль для загрузки данных из JSON.

---

## 📁 Структура проекта

```

.
├── auxiliary_functions.py   # Вспомогательные функции (в т.ч. json_to_py_dict)
├── config.py                # Конфигурационные настройки
├── data.json                # Исходные данные (товары и категории)
├── main.py                  # Основная логика программы
├── pyproject.toml           # Настройки Poetry
├── poetry.lock
├── tests/                   # Тесты проекта
│   ├── **init**.py
│   └── test_main.py
└── README.md                # Документация проекта

````

---

## ⚙️ Описание классов

### **Product**
Класс, описывающий товар.

**Атрибуты:**
- `name` — название товара  
- `description` — описание товара  
- `price` — цена (в рублях)  
- `quantity` — количество на складе  

**Пример создания объекта:**
```python
product = Product("iPhone 15", "Смартфон Apple", 120000, 5)
print(product)
# Product(name = iPhone 15, description = Смартфон Apple, price = 120000, quantity = 5)
````

---

### **Category**

Класс, описывающий категорию товаров.

**Атрибуты:**

* `name` — название категории
* `description` — описание категории
* `products` — список объектов `Product`

**Классовые атрибуты:**

* `count_category` — общее количество созданных категорий
* `general_count_products` — общее количество товаров во всех категориях

**Пример использования:**

```python
products = [
    Product("MacBook Pro", "Ноутбук Apple", 250000, 3),
    Product("iMac", "Моноблок Apple", 300000, 2)
]

category = Category("Ноутбуки", "Компьютеры Apple", products)
print(category)
```

---

## 📚 Загрузка данных из JSON

Функция `json_to_py_dict()` (в модуле `auxiliary_functions.py`) загружает и преобразует JSON (`data.json`) в Python-словарь.

Пример работы в `main.py`:

```python
from auxiliary_functions import json_to_py_dict

data_list = json_to_py_dict()
category_list = []

for category in data_list:
    products_list = [
        Product(
            name=p['name'],
            description=p['description'],
            price=p['price'],
            quantity=p['quantity']
        ) for p in category['products']
    ]
    category_list.append(Category(
        name=category['name'],
        description=category['description'],
        products=products_list
    ))

print(category_list)
```

---

## 🧪 Тестирование

Запуск тестов выполняется через **pytest**:

```bash
pytest -v
```

---

## 🐍 Как запустить проект

1. Убедись, что у тебя установлен **Python 3.12+** и **Poetry**.
2. Установи зависимости:

   ```bash
   poetry install
   ```
3. Активируй виртуальное окружение:

   ```bash
   poetry shell
   ```
4. Запусти основной файл:

   ```bash
   python main.py
   ```

