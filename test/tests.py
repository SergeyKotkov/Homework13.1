import pytest

from utils import Category, Product


@pytest.fixture()
def Category_prod_1():
    return Category('Яблоки', 'сладкие')


def test_Category(Category_prod_1):
    assert Category_prod_1.name == 'Яблоки'
    assert Category_prod_1.description == 'сладкие'


@pytest.fixture()
def Product_prod_1():
    return Product('Яблоки', 'сладкие',  50, 100)

def test_Product(Product_prod_1):
    assert Product_prod_1.name == 'Яблоки'
    assert Product_prod_1.description == 'сладкие'
    assert Product_prod_1.price == 50
    assert Product_prod_1.quantity == 100

def test_total_categories(Category_prod_1):
    assert Category.total_categories > 0

def test_total_uniq_products(Product_prod_1):
    assert Category.total_uniq_products != None
