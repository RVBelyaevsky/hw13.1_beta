import pytest

from main import Category, Product


@pytest.fixture()
def smartfones():
    return Category("Смартфоны", "Описание смартфона", [1, 2, 3])


@pytest.fixture()
def Iphone_15():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_init(smartfones):
    assert smartfones.name == 'Смартфоны'
    assert smartfones.description == 'Описание смартфона'
    assert smartfones.products == [1, 2, 3]
    assert smartfones.count_categories == 1
    assert smartfones.unique_products == 3



def test2_init(Iphone_15):
    assert Iphone_15.name == 'Iphone 15'
    assert Iphone_15.description == '512GB, Gray space'
    assert Iphone_15.price == 210000.0
    assert Iphone_15.quantity == 8

@pytest.fixture()
def count():
   return  Category("Смартфоны", "Описание смартфона", [1, 2, 3])


def test_count_ctg(count):
    assert count.count_categories == 1
    assert count.unique_products == 3
