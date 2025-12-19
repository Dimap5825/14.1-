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
        # приватный
        self.__price = price
        self.quantity = quantity
        self.__display = f'{self.name}, {self.__price}, Остаток: {self.quantity} шт '
        self.info = {'name': self.name, 'description': self.description, 'price': self.__price, 'quantity': self.quantity}
        self._is_initialized = True


    # позволяет сравнивать 2 обьекта
    def __eq__(self, other):
        # если класс не Product сравнивать смысла нет
        if not isinstance(other, Product):
            return False
        # если оба обьекта имеют класс Product то сравнивать их по параметрам
        return (
                self.name == other.name and
                self.description == other.description and
                self.get_price == other.get_price and
                self.quantity == other.quantity
        )

    # определяет как обьект будет выглядить при выходе
    def __repr__(self):
        return f'Product(name = {self.name}, description = {self.description},price = {self.get_price},quantity = {self.quantity})'

#Задание 3 (14.2)
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
            name=data_dict['name'],
            description=data_dict['description'],
            price=data_dict['price'],
            quantity=data_dict['quantity']
        )
        # Начинаем проверку в переданном списке если передан
        if list_of_unique_products:
            # Если есть продукт с таким именем, то меняем информацию о его количестве
            for product in list_of_unique_products:
                # если имя такое же то начинаем обьединять
                if product.name == new_product.name:
                    product.quantity += new_product.quantity
                    if product.get_price < new_product.get_price:
                        product.get_price = new_product.get_price
                    new_product = product
                    return new_product
            # если не нашлось продукта с таким именем то код дойдёт до сюда
            list_of_unique_products.append(new_product)
        return new_product

    # Задание 4 геттер для Product.__price
    # Задание 4

    # в случае если цена равна или ниже нуля, выводите сообщение в консоль
    # “Цена не должна быть нулевая или отрицательная”
    # при этом новую цену устанавливать не нужно.
    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def get_price(self,new_price :int|float = 0):
        if new_price <= 0 :
            print('Цена не должна быть нулевая или отрицательная')
        else:
            if self.__price > new_price:
                # запуск цикла для получения ответа от пользователя
                while True:
                    # если цену хотят снизить запрагиваем ращрешение
                    user_answer = input('Вы хотите понизить цену?\ny (значит yes) или n (значит no) ')
                    # если да меняем цену
                    if user_answer.lower() == 'y':
                        self.__price = new_price
                        break
                    elif user_answer.lower() == 'n':
                        print('Изменение цены отменено')
                        break
                    else:
                        print('неверный ввод, попробуйте заново')

    @property
    def display(self):
        return self.__display



class Category:
    """
    Класс Категория
    """
    # количсетво категорий
    count_category = 0
    # количетво продуктов
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
            # если не пустой
        self.__products = products
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
            self.__products == other.__products
        )

     # чтобы выводилось красиво для разработчика
    def __repr__(self):
        return (
                f'\n   Category(name = {self.name}, description = {self.description},'
                f'products = {self.__products}, count_products = {self.count_products})\n'
                f'Всего категорий:{Category.count_category}\n'
                f'Всего продуктов:{Category.general_count_products})'
        )


    # задание 1 (14.2)
    # добавить продукт
    def add_product(self,product:list[Product]|Product):
        """
        Добавление продукта в список категории
        self: категория(конкретная)
        product : список обьектов типа Product или просто обьект Product
        """
        # если передан просто обьект типа Product
        if isinstance(product,Product):
            self.__products.append(product)
            type(self).general_count_products += 1


        # если передан список с обьектами типа Product
        elif isinstance(product,list):
            for i in product:
                if isinstance(i,Product):
                    self.__products.append(i)
                    type(self).general_count_products += 1





#     Задание 2(14.2)
# Так как вы сделали атрибут со списком товаров приватным,
# то атрибут «список товаров категории» у вас освободился,
# но вы лишили программу возможности выводить список товаров.
# Чтобы вернуть возможность просмотра товаров, нужно реализовать
# Геттер
# который будет выводить список товаров в виде строк в формате:
# "Название продукта, 80 руб. Остаток: 15 шт."

    # свойство
    def display_products_list_fun(self):
        """

        :return: str (общая строка в формате как будто отдельные строки)
        """

        # генератор перебирающий по одному продукту в списке категории
        gener_product = (product.display for product in self.__products)
        return ''.join(gener_product)

    # метод(заменяющий атрибут, потому что мы его сделали приватным)
    @property
    def display_products_list(self):
        return self.display_products_list_fun()


# product_1 = Product('pen_1','описание',45, 1)
# product_2 =Product('pen_2','описание',45, 2)
# product_3 = Product.new_product({'name':'pen','description':'описание_3','price':89,'quantity':3})
# cat_1 = Category(name='pens',description='гелевые',products=[product_1,product_2])
# print(cat_1.display_products_list)
# cat_1.add_product(product=product_3)
# print('\n')
# print(cat_1.display_products_list)
# print('\n')
# print(Category.general_count_products)



cat =  Category(name='drinks', description='carbonated', products=[])
p=  Product(name='Cola', description='foreign', price=66, quantity=123)
cat.add_product(product=p)
# print(cat.display_products_list)
# print(p.price)
# p.get_price = 1