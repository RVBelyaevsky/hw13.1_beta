import pytest

from src.smartfone import Smartfone


@pytest.fixture
def smart():
    return Smartfone('oppo', 'good', 5000.0, 2, 16, 'premium', 256, 'black')


def test_init(smart):
    assert smart.name == 'oppo'

