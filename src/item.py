import csv
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self. price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):

        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        return None


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            raise TypeError('Длина наименования товара превышает 10 символов.')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Создает экземпляры класса Item из данных в файле items.csv и добавляет их в атрибут all.
        """
        cls.all = []
        with open(path, newline='', encoding='cp1251') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)
    @staticmethod
    def string_to_number(s: str) -> int:
        """
        Преобразует строку в число.

        :param s: Строка, которую нужно преобразовать.
        :return: Число, полученное из строки.
        """
        try:
            return math.floor(float(s))
        except ValueError:
            return 0


