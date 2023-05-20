import csv
import unittest
import os

from src.item import Item
from src.keyboard import Keyboard


class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item('test item', 10.0, 5)

    def test_name(self):
        self.assertEqual(self.item.name, 'test item')
        self.item.name = 'new name'
        self.assertEqual(self.item.name, 'new name')
        with self.assertRaises(TypeError):
            self.item.name = 'name is too long'

    def test_calculate_total_price(self):
        self.assertEqual(self.item.calculate_total_price(), 50.0)

    def test_apply_discount(self):
        Item.pay_rate = 0.8
        self.item.apply_discount()
        self.assertEqual(self.item.price, 8.0)

    def test_instantiate_from_csv(self):
        path = 'items.csv'
        with open(path, 'w', newline='', encoding='cp1251') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'price', 'quantity'])
            writer.writerow(['item1', '10.0', '5'])
            writer.writerow(['item2', '20.0', '3'])
        Item.instantiate_from_csv(path)
        self.assertEqual(len(Item.all), 2)
        self.assertEqual(Item.all[0].name, 'item1')
        self.assertEqual(Item.all[0].price, 10.0)
        self.assertEqual(Item.all[0].quantity, 5)
        self.assertEqual(Item.all[1].name, 'item2')
        self.assertEqual(Item.all[1].price, 20.0)
        self.assertEqual(Item.all[1].quantity, 3)
        os.remove(path)

    def test_item_repr(self):
        item = Item('apple', 1.5, 10)
        assert repr(item) == "Item('apple', 1.5, 10)"

    def test_item_str(self):
        item = Item('apple', 1.5, 10)
        assert str(item) == 'apple'

class Keyboard(Item):
    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language

    def get_language(self):
        return self.language

def test_get_language():
    k1 = Keyboard("Logitech", 1000, 5, "RU")
    assert k1.get_language() == "RU"

    k2 = Keyboard("Microsoft", 800, 10)
    assert k2.get_language() == "EN"

    k3 = Keyboard("HP", 1200, 3, "FR")
    assert k3.get_language() == "FR"