class CategoryExpected(Exception):
    """
    класс ошибки для класса Category
    """

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен"):
        self.message = message
        super().__init__(self.message)
