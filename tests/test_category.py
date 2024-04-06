import pytest

from src.product import Product
from src.category import Category


@pytest.fixture()
def smartfones():
    '''категория для теста Category'''
    return Category("Смартфоны", "Описание категории", [Product("oppo", "good phone", 5000.0, 10),
                                                        Product("oppo2", "no good phone", 2000.0, 5)])

@pytest.fixture()
def fruits():
    '''категория для теста fruits'''
    return Category("fruits", "Описание категории", [])

@pytest.fixture()
def Iphone_15():
    '''категория для теста Product'''
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_init(smartfones):
    assert smartfones.name == 'Смартфоны'
    assert smartfones.description == 'Описание категории'
    assert smartfones.count_categories == 1
    assert smartfones.unique_products == 2



def test2_init(Iphone_15):
    assert Iphone_15.name == 'Iphone 15'
    assert Iphone_15.description == '512GB, Gray space'
    assert Iphone_15.price == 210000.0
    assert Iphone_15.quantity == 8

def test_average_price(smartfones):
    assert smartfones.average_price() == 3500.0

def test_average_price(fruits):
    assert fruits.average_price() == 0
