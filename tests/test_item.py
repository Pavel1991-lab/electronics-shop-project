"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

@pytest.mark.parametrize("name, price, quantity, expected_total", [
    ("Смартфон", 10000, 20, 200000),
    ("Ноутбук", 20000, 5, 100000),
])
def test_calculate_total_price(name, price, quantity, expected_total):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == expected_total

@pytest.mark.parametrize("price, expected_discounted_price", [
    (10000, 8000.0),
    (20000, 16000.0),
])
def test_apply_discount(price, expected_discounted_price):
    item = Item("Смартфон", price, 20)
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == expected_discounted_price

def test_all_items():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert len(Item.all) == 2
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].name == "Ноутбук"