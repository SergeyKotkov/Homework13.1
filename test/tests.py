import pytest

from utils import Category, Product


@pytest.fixture()
def Category_prod_1():
    return Category('Яблоки', 'сладкие', ("фрукт", "красные"))


def test_Category(Category_prod_1):
    assert Category_prod_1.name == 'Яблоки'
    assert Category_prod_1.description == 'сладкие'
    assert Category_prod_1.products == ("фрукт", "красные")

@pytest.fixture()
def Product_prod_1():
    return Product('Яблоки', 'сладкие', ("фрукт", "красные"),50, 100)

def test_Product(Product_prod_1):
    assert Product_prod_1.name == 'Яблоки'
    assert Product_prod_1.description == 'сладкие'
    assert Product_prod_1.product == ("фрукт", "красные")
    assert Product_prod_1.price == 50
    assert Product_prod_1.stock == 100



