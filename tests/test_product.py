import pytest

from src.product import Product

@pytest.fixture()
def prod1_dict():
    '''словарь для теста Product'''
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 0
      }


def test_Value_error(prod1_dict):
    with pytest.raises(ValueError):
        Product.create_product(prod1_dict)

